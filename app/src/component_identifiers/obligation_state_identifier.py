from app.classes.processing.scored_components import ScoredPrimitive
from app.src.component_identifiers.interfaces import IScorePrimitives
from app.src.matcher_helper import IGetMatches

from app.classes.spec.sym_situation import ObligationState
from app.src.component_identifiers.helpers.state_name_scorer import IScoreStates
from app.src.component_identifiers.helpers.variable_scorer import IScoreVariables

class ObligationStateIdentifier(IScorePrimitives):
    def __init__(
        self, 
        # state_name_scorer: IScoreStates, 
        # obligation_scorer: IScoreVariables
        matcher: IGetMatches
    ):
        self.__matcher = matcher
        # self.__state_name_scorer = state_name_scorer
        # self.__obligation_scorer = obligation_scorer

    def identify(self, doc) -> ScoredPrimitive:
        return None   

    # def identify_old(self, doc) -> ScoredPrimitive:
    #     state_name, state_score = self.__state_name_scorer.score(doc)

    #     obligation_variable, ob_score = self.__obligation_scorer.score(doc)

    #     score = round(state_score * ob_score, 3)

    #     primitive = ObligationState(state_name, obligation_variable)

    #     return ScoredPrimitive(primitive, score)
    
