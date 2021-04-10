words1 = [{u'confidence': 1.0,
      u'length': 0.599999999999909,
      u'start': 0.0,
      u'word': u'halloween'},
     {u'confidence': 1.0,
      u'length': 0.36000000000012733,
      u'start': 0.7200000000002547,
      u'word': u'um'},
     {u'confidence': 1.0,
      u'length': 0.09000000000014552,
      u'start': 1.080000000000382,
      u'word': u"i'll"},
     {u'confidence': 1.0,
      u'length': 0.1799999999998363,
      u'start': 1.1700000000000728,
      u'word': u'talk'},
     {u'confidence': 1.0,
      u'length': 0.05999999999994543,
      u'start': 1.3500000000003638,
      u'word': u'to'},
     {u'confidence': 1.0,
      u'length': 0.05999999999994543,
      u'start': 1.4100000000003092,
      u'word': u'you'},
     {u'confidence': 1.0,
      u'length': 0.2699999999999818,
      u'start': 1.4700000000002547,
      u'word': u'soon'},
     {u'confidence': 0.263926,
      u'length': 0.23999999999978172,
      u'start': 2.480000000000018,
      u'word': u'uh-huh'},
     {u'confidence': 0.890789,
      u'length': 0.2699999999999818,
      u'start': 4.190000000000055,
      u'word': u'bye'}]



mycall = {"asr":
         [{"start":0.5,
           "words":words1,
           "speaker":"Rep"
          },
          {"start":5,
           "words":words1,
           "speaker":"Rep"
          },
          {"start":10,
           "words":words1,
           "speaker":"Cust"
          },
          {"start":15,
           "words":words1,
           "speaker":"Cust"
          },
          {"start":20,
           "words":words1[:3],
           "speaker":"Rep"
          },
          {"start":22,
           "words":words1,
           "speaker":"Cust"
          }
          
             
         ]}


mycall2 = {"asr":
         [{"start":0.5,
           "words":words1,
           "speaker":"Rep"
          },
          {"start":5,
           "words":words1,
           "speaker":"Cust"
          },
          {"start":10,
           "words":words1,
           "speaker":"Cust"
          },
          {"start":15,
           "words":words1,
           "speaker":"Cust"
          },
          {"start":20,
           "words":words1[:3],
           "speaker":"Rep"
          },
          {"start":22,
           "words":words1,
           "speaker":"Cust"
          }
          
             
         ]}