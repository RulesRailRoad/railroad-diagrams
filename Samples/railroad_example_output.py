sys.stdout.write("<h1>Molecules</h1>\n")


add("Train(state~moving~stopped, track)",
    Diagram(
        Terminal("Train", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("state", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("moving", box_color="khaki"), NonTerminal("stopped", box_color="khaki")))),
    Choice(0, Comment("    "), Terminal("track", box_color='lightblue')),
    )
)

add("TrackSegment(occupancy~free~occupied, signal~green~red, train)",
    Diagram(
        Terminal("TrackSegment", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("occupancy", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("free", box_color="khaki"), NonTerminal("occupied", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("signal", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("green", box_color="khaki"), NonTerminal("red", box_color="khaki")))),
    Choice(0, Comment("    "), Terminal("train", box_color='lightblue')),
    )
)

add("Crossing(state~open~closed, sensor~inactive~active)",
    Diagram(
        Terminal("Crossing", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("state", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("open", box_color="khaki"), NonTerminal("closed", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("sensor", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("inactive", box_color="khaki"), NonTerminal("active", box_color="khaki")))),
    )
)
sys.stdout.write("<h1>Species</h1>\n")


add("Train(state~moving, track)",
    Diagram(
        Terminal("Train", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("state", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("moving", box_color="khaki")))),
    Choice(0, Comment("    "), Terminal("track", box_color='lightblue')),
    )
)

add("TrackSegment(occupancy~free, signal~green, train)",
    Diagram(
        Terminal("TrackSegment", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("occupancy", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("free", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("signal", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("green", box_color="khaki")))),
    Choice(0, Comment("    "), Terminal("train", box_color='lightblue')),
    )
)

add("Crossing(state~open, sensor~inactive)",
    Diagram(
        Terminal("Crossing", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("state", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("open", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("sensor", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("inactive", box_color="khaki")))),
    )
)
sys.stdout.write("<h1>Observables</h1>\n")


add("Train(track!+)",
    Diagram(
        Terminal("Train", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("state", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("moving", box_color="khaki"), NonTerminal("stopped", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Terminal("track", box_color='lightblue', bottom_bind=True, bond_num="+")),
    )
)

add("TrackSegment(occupancy~free)",
    Diagram(
        Terminal("TrackSegment", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("occupancy", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("free", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("signal", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("green", box_color="khaki"), NonTerminal("red", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Terminal("train", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("TrackSegment(signal~red)",
    Diagram(
        Terminal("TrackSegment", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("occupancy", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("free", box_color="khaki"), NonTerminal("occupied", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("signal", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("red", box_color="khaki")))),
    Choice(0, Comment("    "), Terminal("train", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Crossing(state~closed)",
    Diagram(
        Terminal("Crossing", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("state", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("closed", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("sensor", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("inactive", box_color="khaki"), NonTerminal("active", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)
sys.stdout.write("<h1>Reactions</h1>\n")


add("Train(state~moving, track) + TrackSegment(occupancy~free, train, signal~green) -> Train(state~moving, track!1).TrackSegment(occupancy~occupied, train!1, signal~green)",
    Diagram(
        Terminal("Train", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("state", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("moving", box_color="khaki")))),
    Choice(0, Comment("    "), Terminal("track", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="nradded")),
        EndWhiteSpace(),
        Terminal("TrackSegment", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("occupancy", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("free", box_color="khaki"), NonTerminal("occupied", box_color="khaki"))))),
    Choice(0, Comment("    "), Sequence(Terminal("signal", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("green", box_color="khaki")))),
    Choice(0, Comment("    "), Terminal("train", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="nradded")),
    )
)

add("TrackSegment(occupancy~occupied, signal~green) -> TrackSegment(occupancy~occupied, signal~red)",
    Diagram(
        Terminal("TrackSegment", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("occupancy", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("occupied", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("signal", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("green", box_color="khaki"), NonTerminal("red", box_color="khaki"))))),
    Choice(0, Comment("    "), Terminal("train", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Train(state~moving, track!1).TrackSegment(occupancy~occupied, train!1, signal~red) -> Train(state~moving, track) + TrackSegment(occupancy~free, train, signal~red)",
    Diagram(
        Terminal("Train", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("state", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("moving", box_color="khaki")))),
    Choice(0, Comment("    "), Terminal("track", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="nrbroken")),
        EndWhiteSpace(),
        Terminal("TrackSegment", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("occupancy", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "up-arrow", NonTerminal("free", box_color="khaki"), NonTerminal("occupied", box_color="khaki"))))),
    Choice(0, Comment("    "), Sequence(Terminal("signal", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("red", box_color="khaki")))),
    Choice(0, Comment("    "), Terminal("train", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="nrbroken")),
    )
)

add("TrackSegment(occupancy~free, signal~red) -> TrackSegment(occupancy~free, signal~green)",
    Diagram(
        Terminal("TrackSegment", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("occupancy", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("free", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("signal", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "up-arrow", NonTerminal("green", box_color="khaki"), NonTerminal("red", box_color="khaki"))))),
    Choice(0, Comment("    "), Terminal("train", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Train(state~moving) + Crossing(sensor~inactive) -> Train(state~moving) + Crossing(sensor~active)",
    Diagram(
        Terminal("Train", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("state", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("moving", box_color="khaki")))),
    Choice(0, Comment("    "), Terminal("track", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("Crossing", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("state", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("open", box_color="khaki"), NonTerminal("closed", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("sensor", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("inactive", box_color="khaki"), NonTerminal("active", box_color="khaki"))))),
    )
)

add("Crossing(state~open, sensor~active) -> Crossing(state~closed, sensor~active)",
    Diagram(
        Terminal("Crossing", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("state", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("open", box_color="khaki"), NonTerminal("closed", box_color="khaki"))))),
    Choice(0, Comment("    "), Sequence(Terminal("sensor", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("active", box_color="khaki")))),
    )
)

add("Crossing(state~closed, sensor~active) -> Crossing(state~open, sensor~inactive)",
    Diagram(
        Terminal("Crossing", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("state", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "up-arrow", NonTerminal("open", box_color="khaki"), NonTerminal("closed", box_color="khaki"))))),
    Choice(0, Comment("    "), Sequence(Terminal("sensor", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "up-arrow", NonTerminal("inactive", box_color="khaki"), NonTerminal("active", box_color="khaki"))))),
    )
)
