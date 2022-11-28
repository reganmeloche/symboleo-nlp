from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensAfter, PredicateFunctionWHappensBefore, PredicateFunctionWHappensBeforeEvent
from app.classes.spec.sym_point import PointAtomParameterDotExpression, PointFunction, PointAtomContractEvent
from app.classes.spec.sym_event import ContractEvent, VariableEvent
from app.classes.spec.helpers import TimeUnitStr, TimeValueInt, VariableDotExpression
from app.src.rules.shared.configs import PredicateExtractorConfig
from app.src.rules.shared.case_obj import CaseObj
from app.src.rules.contract_spec.timeframe.timeframe_matcher import get_tf_matcher

from app.classes.spec.predicate_function import PredicateFunction

from app.src.rules.shared.interfaces import IBuildPredicateExtractor, IExtractPredicates
from app.src.rules.contract_spec.predicate_extractor import PredicateExtractor
from app.src.rules.contract_spec.dynamic_constructor_builder import DynamicConstructorBuilder


# e.g. for payment:
# paid_event = contract_template.domain_model.events['paid'].to_obj()
# template = PredicateFunctionHappens(paid_event)


class TimeFrameExtractorBuilder(IBuildPredicateExtractor):
    @staticmethod
    def build(nlp, template: PredicateFunction) -> IExtractPredicates:
        matcher = get_tf_matcher(nlp)
        
        case_dict = {
            'within_time_period': CaseObj([PointFunction], PredicateFunctionWHappensBefore),
            'before_date': CaseObj([PointAtomParameterDotExpression], PredicateFunctionWHappensBefore),
            'after_date': CaseObj([PointAtomParameterDotExpression], PredicateFunctionHappensAfter),
            'before_event': CaseObj([VariableEvent], PredicateFunctionWHappensBeforeEvent),
            'after_event': CaseObj([None], None),
            'between_date_and_date': CaseObj([None], None),
            'within_time_period_of_event': CaseObj([None], None)
        }

        # Can maybe just do this for all primitives... just loop through them
        primitive_dict = {
            'time_value_int': TimeValueInt,
            'time_unit_string': TimeUnitStr,
            'point_vde': VariableDotExpression,
            'event_vde': VariableDotExpression
        }

        contract_event = ContractEvent('activated')
        default_components = [
            PointAtomContractEvent(contract_event)
        ]

        config = PredicateExtractorConfig(template, matcher, case_dict, primitive_dict, default_components)
        
        dynamic_constructor = DynamicConstructorBuilder.build()
        
        return PredicateExtractor(nlp, config, dynamic_constructor)
