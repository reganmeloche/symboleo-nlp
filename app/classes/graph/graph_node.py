import copy

PROP_TYPE = 'prop'
SUBCLASS_TYPE = 'subclass'

class GraphNode:
    name: str = ''
    node_type: str = '' # subclass or prop
    subclasses: list[str] = [] 
    props: list[str] = [] 

    def __init__(self, name, node_type, subclasses, props):
        self.name = name
        self.node_type = node_type
        self.subclasses = copy.deepcopy(subclasses)
        self.props = copy.deepcopy(props)

    def __eq__(self, other): 
        if not isinstance(other, GraphNode):
            return NotImplemented

        return self.name == other.name and \
                self.node_type == other.node_type and \
                self._eq_list(self.subclasses, other.subclasses) and \
                self._eq_list(self.props, other.props)
    
    def _eq_list(self, a, b):
        if len(a) != len(b):
            return False
        
        return set(a) == set(b)
        

    def print_me(self, d=0):
        print(f'{self.name}')
        s_list = ','.join(self.subclasses)
        p_list = ','.join(self.props)
        print(f'-- s: {s_list}')
        print(f'-- p: {p_list}')
        
# TODO: Update this!
test_graph = {
    ## ROOTS ##
    'PAtom': GraphNode(
        'PAtom', 
        'ROOT',
        [
            'PAtomPredicate',
            #...
        ],
        []
    ),
    'PAtomPredicate': GraphNode(
        'PAtomPredicate',
        SUBCLASS_TYPE,
        [],
        ['PredicateFunction']
    ),
    'PredicateFunction': GraphNode(
        'PredicateFunction',
        PROP_TYPE,
        [
            'PredicateFunctionHappens', 
            'PredicateFunctionHappensWithin', 
            'PredicateFunctionWHappensBefore', 
            'PredicateFunctionWHappensBeforeEvent',
            'PredicateFunctionHappensAfter',
            'PredicateFunctionOccurs',
            ### more...
        ],
        []
    ),
    
    ## Predicate Functions ##
    'PredicateFunctionHappens': GraphNode(
        'PredicateFunctionHappens',
        SUBCLASS_TYPE,
        [],
        ['SymEvent']
    ),
    'PredicateFunctionWHappensBefore': GraphNode(
        'PredicateFunctionWHappensBefore',
        SUBCLASS_TYPE,
        [],
        ['SymEvent', 'SymPoint']
    ),
    'PredicateFunctionHappensWithin': GraphNode(
        'PredicateFunctionHappensWithin',
        SUBCLASS_TYPE,
        [],
        ['SymEvent', 'SymInterval']
    ),
    'PredicateFunctionWHappensBeforeEvent': GraphNode(
        'PredicateFunctionWHappensBeforeEvent',
        SUBCLASS_TYPE,
        [],
        ['SymEvent', 'SymEvent']
    ),
    'PredicateFunctionHappensAfter': GraphNode(
        'PredicateFunctionHappensAfter',
        SUBCLASS_TYPE,
        [],
        ['SymEvent', 'SymPoint']
    ),
    'PredicateFunctionOccurs': GraphNode(
        'PredicateFunctionOccurs',
        SUBCLASS_TYPE,
        [],
        ['SymSituation', 'SymInterval']
    ),

    ## SymPoint ##
    'SymPoint': GraphNode(
        'SymPoint',
        PROP_TYPE,
        ['Point'],
        []
    ),
    'Point': GraphNode(
        'Point',
        SUBCLASS_TYPE,
        [],
        ['PointExpression'],
    ),
    'PointExpression': GraphNode(
        'PointExpression',
        PROP_TYPE,
        ['PointFunction', 'PointAtom'],
        []
    ),
    'PointFunction': GraphNode(
        'PointFunction',
        SUBCLASS_TYPE,
        [],
        ['PointAtom', 'TimeValue', 'TimeUnit']
    ),
    'PointAtom': GraphNode(
        'PointAtom',
        SUBCLASS_TYPE,
        ['PointAtomParameterDotExpression', 'PointAtomObligationEvent', 'PointAtomPowerEvent', 'PointAtomContractEvent'],
        []
    ),
    'TimeValue': GraphNode(
        'TimeValue',
        PROP_TYPE,
        ['TimeValueInt', 'TimeValueVariable'],
        []
    ),
    'TimeValueInt': GraphNode(
        'TimeValueInt',
        SUBCLASS_TYPE,
        [],
        []
    ),
    'TimeValueVariable': GraphNode(
        'TimeValueVariable',
        SUBCLASS_TYPE,
        [],
        ['VariableDotExpression']
    ),
    'TimeUnit': GraphNode(
        'TimeUnit',
        PROP_TYPE,
        ['TimeUnitStr'],
        []
    ),
    'TimeUnitStr': GraphNode(
        'TimeUnitStr',
        SUBCLASS_TYPE,
        [],
        []
    ),
    'PointAtomParameterDotExpression': GraphNode(
        'PointAtomParameterDotExpression',
        SUBCLASS_TYPE,
        [],
        ['VariableDotExpression']
    ),
    'PointAtomObligationEvent': GraphNode(
        'PointAtomObligationEvent',
        SUBCLASS_TYPE,
        [],
        ['ObligationEvent']
    ),
    'PointAtomPowerEvent': GraphNode(
        'PointAtomPowerEvent',
        SUBCLASS_TYPE,
        [],
        ['PowerEvent']
    ),
    'PointAtomContractEvent': GraphNode(
        'PointAtomContractEvent',
        SUBCLASS_TYPE,
        [],
        ['ContractEvent']
    ),

    ## SymInterval ##
    'SymInterval': GraphNode(
        'SymInterval',
        PROP_TYPE,
        ['Interval'],
        []
    ),
    'Interval': GraphNode(
        'Interval',
        SUBCLASS_TYPE,
        [],
        ['IntervalExpression']
    ),
    'IntervalExpression': GraphNode(
        'IntervalExpression',
        PROP_TYPE,
        ['SituationExpression', 'IntervalFunction'],
        []
    ),
    'SituationExpression': GraphNode(
        'SituationExpression',
        SUBCLASS_TYPE,
        [],
        ['SymSituation']
    ),
    'IntervalFunction': GraphNode(
        'IntervalFunction',
        SUBCLASS_TYPE,
        [],
        ['PointExpression', 'PointExpression']
    ),

    ## SymEvent ##
    'SymEvent': GraphNode(
        'SymEvent',
        PROP_TYPE,
        ['VariableEvent', 'PowerEvent', 'ObligationEvent', 'ContractEvent'],
        []
    ),
    'VariableEvent': GraphNode(
        'VariableEvent',
        SUBCLASS_TYPE,
        [],
        ['VariableDotExpression']
    ),
    'PowerEvent': GraphNode(
        'PowerEvent',
        SUBCLASS_TYPE,
        [],
        []
    ),
    'ObligationEvent': GraphNode(
        'ObligationEvent',
        SUBCLASS_TYPE,
        [],
        []
    ),
    'ContractEvent': GraphNode(
        'ContractEvent',
        SUBCLASS_TYPE,
        [],
        []
    ),

    ## SymSituation ##
    'SymSituation': GraphNode(
        'SymSituation',
        PROP_TYPE,
        ['ObligationState', 'PowerState', 'ContractState'],
        []
    ),
    'ObligationState': GraphNode(
        'ObligationState',
        SUBCLASS_TYPE,
        [],
        []
    ),
    'PowerState': GraphNode(
        'PowerState',
        SUBCLASS_TYPE,
        [],
        []
    ),
    'ContractState': GraphNode(
        'ContractState',
        SUBCLASS_TYPE,
        [],
        []
    ),

    ## Variable ##
    'VariableDotExpression': GraphNode(
        'VariableDotExpression',
        PROP_TYPE,
        [],
        []
    )
}
