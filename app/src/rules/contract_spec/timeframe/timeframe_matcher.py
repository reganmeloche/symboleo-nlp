from spacy.matcher import Matcher

# Can combine different spacy approaches - doesnt need to just be one
# e.g. combine the token matcher with the dependency matcher
# Some are for validation, some are for extracting specific props, some are for control flow.


# Will probably make this a class with some more rules and properties
## Three key matches: validation, cases, primitives
## Although validation may be covered by cases...
def get_tf_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    # Validation Patterns
    validation_patterns = [
    ]
    matcher.add('validation', validation_patterns)

    # Cases
    within_time_period_pattern = [
        [{"LOWER": {'IN': ['within']}}, {"ENT_TYPE": 'DATE', "OP": "+"}],
    ]

    before_date_pattern = [
        [{"LOWER": {'IN': ['before', 'by', 'on']}}, {"ENT_TYPE": 'DATE', "OP": "+"}],
    ]

    # This is where I add my own preprocessing to pick up domain events...
    ## An event may be more than just a token though...
    before_event_pattern = [
        [{"LOWER": {'IN': ['before']}}, {"LOWER": 'the', "OP": "?"}, {"ENT_TYPE": 'DOMAIN_EVENT', "OP": "+"}],
    ]

    after_date_pattern = [
        [{"LOWER": {'IN': ['after']}}, {"ENT_TYPE": 'DATE', "OP": "+"}],
    ]

    between_dates_pattern = [
        [{"LOWER": {'IN': ['between']}}, {"ENT_TYPE": 'DATE', "OP": "+"}, {"LOWER": "and"}, {"ENT_TYPE": 'DATE', "OP": "+"} ],
    ]

    until_adp_event_pattern = [
        [{"LOWER": {'IN': ['until']}}, {"ENT_TYPE": 'DATE', "OP": "+"}, {"LOWER": {'IN': ['after']}, "POS": "ADP"}, {"ENT_TYPE": "DOMAIN_EVENT", "OP": "+"} ],
    ]

    matcher.add("within_time_period", within_time_period_pattern)
    matcher.add("before_date", before_date_pattern)
    matcher.add("before_event", before_event_pattern)
    matcher.add("after_date", after_date_pattern)
    matcher.add("between_dates", between_dates_pattern)
    matcher.add("until_adp_event", until_adp_event_pattern)

    return matcher