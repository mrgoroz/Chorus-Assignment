import add_turns
import call_data

at = add_turns.AddTurnsPlugin(call_data.mycall)

def test_get_turns_for_speaker():
    res = at.get_turns_for_speaker(add_turns.REP, add_turns.MAX_GAP)
    assert len(res) == 3

def test_get_turns_call():
    res = at.get_turns_call(add_turns.MAX_GAP)
    assert len(res) == 2

# at.run()
# for ut in at.call_data['asr']:
#     print(ut)