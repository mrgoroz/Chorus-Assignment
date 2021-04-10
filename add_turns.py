#!/usr/bin/env python


"""Adds turn data to utterances Fused consecutive utterances into a turn if gap is smaller than maxGap parameter (
execpt for edge cases of really short utterances) """
CUST = "Cust"
REP = "Rep"
MAX_GAP = 4


class AddTurnsPlugin:

    def __init__(self, call_data):
        self.call_data = call_data

    """
    Returns list of turns for one speaker
    """

    def get_turns_for_speaker(self, dir, maxgap=MAX_GAP):
        turns_stack = [(ut["start"], ut["start"] + ut["words"][-1]["start"] + ut["words"][-1]["length"], [ut["start"]])
                       for ut in self.call_data["asr"] if ut["speaker"] == dir]
        last_count = len(turns_stack)
        while len(turns_stack) != last_count:
            turn = turns_stack[0]
            turn2 = turns_stack[-1]
            if turn2[1] + min(maxgap, turn2[1] - turn2[0] + 1) > turn[0]:
                turns_stack.append((turn2[0], turn[1], turn2[2] + turn[2]))
        return turns_stack

    def get_turns_call(self, maxgap=4):
        rep_turns = self.get_turns_for_speaker(REP, maxgap=maxgap)
        cust_turns = self.get_turns_for_speaker(CUST, maxgap=maxgap)
        return {REP: rep_turns, CUST: cust_turns}

    def run(self):
        turns_data = self.get_turns_call(self.call_data)

        turns_data_transformed = {REP: {}, CUST: {}}
        for speaker, turns in turns_data.items():
            for ind, curr_turn in enumerate(turns):
                for ts in curr_turn[2]:
                    turns_data_transformed[speaker][ts] = ("%s_%d" % (speaker, ind), curr_turn[1] - curr_turn[0], -1.0)

        for ut in self.call_data["asr"]:
            ut["turn_id"] = turns_data_transformed[ut["speaker"]][ut["start"]][0]
            ut["turn_length"] = turns_data_transformed[ut["speaker"]][ut["start"]][1]
