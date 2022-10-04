from app.classes.spec.symboleo_spec import Obligation
from app.src.matchers.interfaces import IMatcher
from app.src.norm_proposition_updater import IUpdateNormPropositions


class IConvertSentenceToObligation:
    def convert(self, sentence: str, obligation: Obligation, selected_component: str) -> Obligation:
        raise NotImplementedError()

class SentenceObligationConverter(IConvertSentenceToObligation):
    def __init__(
        self, 
        nlp,
        matchers: list[IMatcher],
        norm_updater: IUpdateNormPropositions
    ):
        self.__nlp = nlp
        self.__matchers = matchers
        self.__norm_updater = norm_updater

    def convert(self, sentence: str, obligation: Obligation, selected_component: str) -> Obligation:
        # NLP pipeline
        doc = self.__nlp(sentence)

        # Attempt to construct a predicate from the matchers
        ## Currently this is greedy. Can potentially attach a score to each predicate attempt and evaluate.
        for next_matcher in self.__matchers:
            new_atom = next_matcher.try_match(doc)
            if new_atom:
                result = self.__norm_updater.update(obligation, selected_component, new_atom)
                return result

        # No matches found => invalid entry
        raise ValueError()