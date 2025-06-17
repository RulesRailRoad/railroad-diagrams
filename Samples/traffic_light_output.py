sys.stdout.write("<h1>Molecules</h1>\n")


add("TrafficLight(green~on~off, yellow~on~off, red~on~off)",
    Diagram(
        Terminal("TrafficLight", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("green", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("on", box_color="khaki"), NonTerminal("off", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("yellow", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("on", box_color="khaki"), NonTerminal("off", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("red", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("on", box_color="khaki"), NonTerminal("off", box_color="khaki")))),
    )
)
sys.stdout.write("<h1>Species</h1>\n")


add("TrafficLight(green~on,yellow~off,red~off)",
    Diagram(
        Terminal("TrafficLight", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("green", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("on", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("yellow", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("off", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("red", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("off", box_color="khaki")))),
    )
)
sys.stdout.write("<h1>Observables</h1>\n")


add("TrafficLight(green~on)",
    Diagram(
        Terminal("TrafficLight", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("green", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("on", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("yellow", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("on", box_color="khaki"), NonTerminal("off", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("red", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("on", box_color="khaki"), NonTerminal("off", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)
sys.stdout.write("<h1>Reactions</h1>\n")


add("TrafficLight(green~on, yellow~off, red~off) -> TrafficLight(green~off, yellow~on, red~off)",
    Diagram(
        Terminal("TrafficLight", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("green", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("on", box_color="khaki"), NonTerminal("off", box_color="khaki"))))),
    Choice(0, Comment("    "), Sequence(Terminal("yellow", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "up-arrow", NonTerminal("on", box_color="khaki"), NonTerminal("off", box_color="khaki"))))),
    Choice(0, Comment("    "), Sequence(Terminal("red", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("off", box_color="khaki")))),
    )
)

add("TrafficLight(green~off, yellow~off, red~on) -> TrafficLight(green~on, yellow~off, red~off)",
    Diagram(
        Terminal("TrafficLight", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("green", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "up-arrow", NonTerminal("on", box_color="khaki"), NonTerminal("off", box_color="khaki"))))),
    Choice(0, Comment("    "), Sequence(Terminal("yellow", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("off", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("red", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("on", box_color="khaki"), NonTerminal("off", box_color="khaki"))))),
    )
)

add("TrafficLight(green~off, yellow~on, red~off) -> TrafficLight(green~off, yellow~off, red~on)",
    Diagram(
        Terminal("TrafficLight", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("green", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("off", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("yellow", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("on", box_color="khaki"), NonTerminal("off", box_color="khaki"))))),
    Choice(0, Comment("    "), Sequence(Terminal("red", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "up-arrow", NonTerminal("on", box_color="khaki"), NonTerminal("off", box_color="khaki"))))),
    )
)
