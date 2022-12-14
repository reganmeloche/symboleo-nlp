from app.classes.contract_update_request import ContractUpdateRequest
from app.classes.processing.scored_components import ScoredPrimitive
from app.src.component_identifiers.interfaces import IScorePrimitives
from app.src.matcher_helper import IGetMatches

from app.classes.spec.helpers import TimeValueInt

class TimeValueIntScorer(IScorePrimitives):
    def __init__(
        self,
        matcher: IGetMatches
    ):
        self.__matcher = matcher

    def score(self, req: ContractUpdateRequest) -> ScoredPrimitive:
        doc = req.doc
        pattern = [
            [{"POS": "NUM", "DEP": "nummod", "ENT_TYPE": "DATE" }],
        ]
        match = self.__matcher.match(pattern, doc)

        if match:
            return ScoredPrimitive(TimeValueInt(match.text), 1)
        
        return None

    

    # TODO: Should likely focus on spacy "entities" here
    # TODO: May also want to convert anything to actual numbers. This could be a prepo step - assumption?
    ## numerizer - https://spacy.io/universe/project/numerizer
    ## Assumes only one time point...
    def identify_old(self, doc) -> ScoredPrimitive:
        # Look for numbers that are close to time units?
        target1 = [x for x in doc if x.dep_ == 'nummod' and x.ent_type_ in ['TIME', 'DATE']]

        target2 = [x for x in doc if x.dep_ == 'nummod']

        target3 = [x for x in doc if x.pos_ == 'NUM']

        if len(target1) > 0:
            primitive = TimeValueInt(target1[0].text)
            score = 1
        elif len(target2) > 0:
            primitive = TimeValueInt(target2[0].text)
            score = 0.7
        elif len(target3) > 0:
            primitive = TimeValueInt(target3[0].text)
            score = 0.2
        else:
            primitive = TimeValueInt(0)
            score = 0

        return ScoredPrimitive(primitive, score)
    
