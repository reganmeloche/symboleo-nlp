import unittest
from unittest.mock import MagicMock
from app.src.primitive_identifiers.event_scorer import EventScorer
from tests.helpers.test_nlp import TestNLP

class EventScorerTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()

        d1 = {
            'be': 'be'
        }
        d2 = {
            'ate': 'eat'
        }
        dict_set = [
            (d1, 1),
            (d2, 0.5)
        ]
        self.sut = EventScorer(dict_set)
        

    def test_event_scorer1(self):
        sentence = 'this is a test'
        doc = self.nlp(sentence)

        result = self.sut.score(doc)
        self.assertEqual(result[0], 'be')
        self.assertEqual(result[1], 1)
    

    def test_event_scorer2(self):
        sentence = 'Bob has eaten three apples.'
        doc = self.nlp(sentence)

        result = self.sut.score(doc)
        self.assertEqual(result[0], 'ate')
        self.assertEqual(result[1], 0.5)
    
    
    def test_event_scorer3(self):
        sentence = 'The birds gathered on the tree'
        doc = self.nlp(sentence)

        result = self.sut.score(doc)
        self.assertEqual(result[0], '')
        self.assertEqual(result[1], 0)


        

        
  
  
if __name__ == '__main__':
    unittest.main()