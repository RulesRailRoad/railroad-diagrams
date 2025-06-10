sys.stdout.write("<h1>Molecules</h1>\n")


add("EGFR(ecd,tmd,y1068~u~p,y1173~u~p)",
    Diagram(
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki")))),
    )
)

add("EGF(rb)",
    Diagram(
        Terminal("EGF", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("rb", box_color='lightblue')),
    )
)

add("Grb2(sh2,sos)",
    Diagram(
        Terminal("Grb2", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("sh2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("sos", box_color='lightblue')),
    )
)

add("Shc(sh3,Y773~p~u)",
    Diagram(
        Terminal("Shc", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("sh3", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("Y773", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("p", box_color="khaki"), NonTerminal("u", box_color="khaki")))),
    )
)
sys.stdout.write("<h1>Species</h1>\n")


add("EGF(rb)",
    Diagram(
        Terminal("EGF", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("rb", box_color='lightblue')),
    )
)

add("EGFR(ecd,tmd,y1068~u,y1173~u)",
    Diagram(
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki")))),
    )
)

add("Shc(sh3,Y773~u)",
    Diagram(
        Terminal("Shc", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("sh3", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("Y773", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki")))),
    )
)

add("EGF(rb!1).EGFR(ecd!1,tmd,y1068~u!2,y1173~u).Shc(sh3,Y773~u!2)",
    Diagram(
        Terminal("EGF", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("rb", box_color='lightblue', bottom_bind=True, bond_num="1")),
        EndWhiteSpace(),
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue', bottom_bind=True, bond_num="1")),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki", bottom_bind=True, bond_num="2")))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki")))),
        EndWhiteSpace(),
        Terminal("Shc", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("sh3", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("Y773", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki", bottom_bind=True, bond_num="2")))),
    )
)
sys.stdout.write("<h1>Observables</h1>\n")


add("EGFR()",
    Diagram(
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)

add("EGF()",
    Diagram(
        Terminal("EGF", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("rb", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Shc()",
    Diagram(
        Terminal("Shc", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("sh3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y773", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("p", box_color="khaki"), NonTerminal("u", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)

add("EGFR(tmd!+)",
    Diagram(
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)

add("EGFR(y1068~u~p!+)",
    Diagram(
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, bond_num="+")))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)

add("EGFR(y1173~u~p!+)",
    Diagram(
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, bond_num="+")))),
    )
)

add("EGFR(y1068~p!?) @M",
    Diagram(
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("p", box_color="khaki", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)

add("Shc(Y773~p!?)",
    Diagram(
        Terminal("Shc", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("sh3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y773", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("p", box_color="khaki", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
    )
)
sys.stdout.write("<h1>Reactions</h1>\n")


add("EGF(rb) + EGFR(ecd,tmd) <-> EGF(rb!1).EGFR(ecd!1,tmd)",
    Diagram(
        Terminal("EGF", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("rb", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
        EndWhiteSpace(),
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)

add("EGFR(ecd!+,tmd) + EGFR(ecd!+,tmd) <-> EGFR(ecd!+,tmd!1)%1.EGFR(ecd!+,tmd!1)",
    Diagram(
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
        EndWhiteSpace(),
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)

add("EGFR(y1173~p) -> EGFR(y1173~u)",
    Diagram(
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "up-arrow", NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki"))))),
    )
)

add("EGFR(tmd!+,y1068~u) -> EGFR(tmd!+,y1068~p)",
    Diagram(
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki"))))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)

add("EGFR(tmd!+,y1173~u) -> EGFR(tmd!+,y1173~p)",
    Diagram(
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki"))))),
    )
)

add("EGFR(y1068~p) -> EGFR(y1068~u)",
    Diagram(
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "up-arrow", NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki"))))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)

add("EGFR(y1173~p) + Shc(sh3,Y773~u) <-> EGFR(y1173~p!1).Shc(sh3!1,Y773~u)",
    Diagram(
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("p", box_color="khaki", bottom_bind=True, bond_num="1", bond_type="radded")))),
        EndWhiteSpace(),
        Terminal("Shc", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("sh3", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Sequence(Terminal("Y773", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki")))),
    )
)

add("EGFR(y1173~p!1).Shc(sh3!1,Y773~u) <-> EGFR(y1173~p!1).Shc(sh3!1,Y773~p)",
    Diagram(
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("p", box_color="khaki", bottom_bind=True, bond_num="1")))),
        EndWhiteSpace(),
        Terminal("Shc", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("sh3", box_color='lightblue', bottom_bind=True, bond_num="1")),
    Choice(0, Comment("    "), Sequence(Terminal("Y773", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "up-arrow", NonTerminal("p", box_color="khaki"), NonTerminal("u", box_color="khaki"))))),
    )
)

add("Shc(sh3,Y773~p) -> Shc(sh3,Y773~u)",
    Diagram(
        Terminal("Shc", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("sh3", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("Y773", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("p", box_color="khaki"), NonTerminal("u", box_color="khaki"))))),
    )
)

add("EGFR(y1173~p) + Shc(sh3,Y773~p) <-> EGFR(y1173~p!1).Shc(sh3!1,Y773~p)",
    Diagram(
        Terminal("EGFR", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("u", box_color="khaki"), NonTerminal("p", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("p", box_color="khaki", bottom_bind=True, bond_num="1", bond_type="radded")))),
        EndWhiteSpace(),
        Terminal("Shc", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("sh3", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Sequence(Terminal("Y773", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("p", box_color="khaki")))),
    )
)
