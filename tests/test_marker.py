from trainer.marker import Pitfall, Point, mark, phrase_match, tokens


def test_paraphrase_and_spelling():
    pts = [Point("hot to cold", ["hot to cold", "higher temperature to lower temperature", "hotter to colder"])]
    assert mark("Energy goes from the hoter object to the colder one", pts).passed
    assert mark("from the body at the higher temprature to the body at a lower temperature", pts).passed
    assert not mark("Heat moves between them", pts).passed


def test_order_free_within_window_but_not_across_sentence():
    assert phrase_match(tokens("the water becomes a lot less dense"), "less dense")
    assert phrase_match(tokens("its density is lower"), "lower density")
    assert not phrase_match(tokens("less light comes in. The dense fog stays"), "less dense", window=2)


def test_pitfall_is_ordered_and_tight():
    pits = [Pitfall(["cold to hot"], "wrong way")]
    pts = [Point("direction", ["hot to cold"])]
    assert mark("energy flows from cold to hot", pts, pits).pitfalls == ["wrong way"]
    assert not mark("the cold body gains energy from the hot body", pts, pits).pitfalls   # 'cold ... hot' far apart, not the pitfall
    assert mark("from hot to cold", pts, pits).passed


def test_min_points_and_short_answers():
    pts = [Point("a", ["expands"]), Point("b", ["less dense"]), Point("c", ["rises"])]
    r = mark("it expands and rises", pts, min_points=2)
    assert r.passed and r.score == "2 / 3" and r.missed == ["b"]
    assert not mark("it expands", pts, min_points=2).passed
    r = mark("rises", pts, min_points=2)
    assert r.too_short and not r.passed
    assert mark("Conduction.", [Point("c", ["conduction"])]).passed          # one word is enough for a 'name it' question
    assert not mark("", [Point("c", ["conduction"])]).passed


def test_negated_pitfall_is_not_flagged():
    pits = [Pitfall(["energy is destroyed", "energy is lost"], "no")]
    pts = [Point("p", ["thermal"])]
    assert mark("energy is not destroyed, it becomes thermal", pts, pits).passed
    assert mark("energy is never lost, it becomes thermal", pts, pits).passed
    assert not mark("energy is destroyed and becomes thermal", pts, pits).passed


def test_physics_near_homographs_are_kept_apart():
    assert not phrase_match(tokens("conduction"), "convection")
    assert not phrase_match(tokens("convection"), "conduction")
    assert phrase_match(tokens("convektion"), "convection")
    assert phrase_match(tokens("conducton"), "conduction")
    assert not phrase_match(tokens("less dense"), "denser", exact=True)
    assert not phrase_match(tokens("the emitter"), "omitted")


def test_symbols_hyphens_and_directions():
    # subscripts read as digits, hyphenated words split (but non- words stay whole), into != out of
    assert phrase_match(tokens("1/R = 1/R₁ + 1/R₂"), "1/r = 1/r1 + 1/r2")
    assert phrase_match(tokens("the high-resistance element"), "high resistance")
    assert tokens("non-magnetic") == ["non-magnetic"]
    assert not phrase_match(tokens("out of the page"), "into the page")
    assert phrase_match(tokens("current flows into the page"), "into the page")
