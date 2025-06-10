sys.stdout.write("<h1>Molecules</h1>\n")


add("R(DD,Y1~U~P,Y2~P)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki")))),
    )
)

add("S(NSH2~C~O,CSH2,PTP~C~O)",
    Diagram(
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("C", box_color="khaki"), NonTerminal("O", box_color="khaki")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("C", box_color="khaki"), NonTerminal("O", box_color="khaki")))),
    )
)
sys.stdout.write("<h1>Species</h1>\n")


add("S(NSH2~C,CSH2,PTP~C)",
    Diagram(
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("C", box_color="khaki")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("C", box_color="khaki")))),
    )
)

add("R(DD!1,Y1~U,Y2~P).R(DD!1,Y1~U,Y2~P)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bond_num="1")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki")))),
        EndWhiteSpace(),
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bond_num="1")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki")))),
    )
)
sys.stdout.write("<h1>Observables</h1>\n")


add("R(Y1~P!?)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
    )
)
sys.stdout.write("<h1>Reactions</h1>\n")


add("R(DD!+,Y1~U) -> R(DD!+,Y1~P)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki"))))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
    )
)

add("S(NSH2~C,PTP~C) <-> S(NSH2~O,PTP~O)",
    Diagram(
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("C", box_color="khaki"), NonTerminal("O", box_color="khaki"))))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("C", box_color="khaki"), NonTerminal("O", box_color="khaki"))))),
    )
)

add("R(Y2~P) + S(CSH2) <-> R(Y2~P!1).S(CSH2!1)  kon_CSH2,koff_CSH2  exclude_reactants(2,R)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1", bond_type="radded")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("C", box_color="khaki"), NonTerminal("O", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("C", box_color="khaki"), NonTerminal("O", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)

add("R(Y2~P) + S(NSH2~O) <-> R(Y2~P!1).S(NSH2~O!1)  kon_NSH2,koff_NSH2  exclude_reactants(2,R)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1", bond_type="radded")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="1", bond_type="radded")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("C", box_color="khaki"), NonTerminal("O", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)

add("R(Y1~P) + S(PTP~O) <-> R(Y1~P!1).S(PTP~O!1)  kon_PTP,koff_PTP  exclude_reactants(2,R)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1", bond_type="radded")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("C", box_color="khaki"), NonTerminal("O", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="1", bond_type="radded")))),
    )
)

add("R(Y1~P!1).S(PTP~O!1) -> R(Y1~U) + S(PTP~O)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "up-arrow", NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1", bond_type="nrbroken"))))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("C", box_color="khaki"), NonTerminal("O", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="1", bond_type="nrbroken")))),
    )
)

add("R(Y1~P!1).S(PTP~O!1) -> R(Y1~U).S(PTP~O)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "up-arrow", NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1", bond_type="nrbroken"))))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("C", box_color="khaki"), NonTerminal("O", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="1", bond_type="nrbroken")))),
    )
)

add("R(Y2~P).S(NSH2~O,CSH2!+,PTP~O) <-> R(Y2~P!1).S(NSH2~O!1,CSH2!+,PTP~O)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1", bond_type="radded")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="1", bond_type="radded")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki")))),
    )
)

add("R(Y1~P,Y2~P!1).S(NSH2~O,CSH2!1,PTP~O) <-> R(Y1~P!2,Y2~P!1).S(NSH2~O,CSH2!1,PTP~O!2)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="2", bond_type="radded")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bond_num="1")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="2", bond_type="radded")))),
    )
)

add("R(Y1~P).R(Y2~P!1).S(NSH2~O,CSH2!1,PTP~O) <-> R(Y1~P!2).R(Y2~P!1).S(NSH2~O,CSH2!1,PTP~O!2)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="2", bond_type="radded")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        EndWhiteSpace(),
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bond_num="1")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="2", bond_type="radded")))),
    )
)

add("R(Y2~P).S(NSH2~O!+,CSH2,PTP~O) <-> R(Y2~P!1).S(NSH2~O!+,CSH2!1,PTP~O)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1", bond_type="radded")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="+")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki")))),
    )
)

add("R(Y1~P).R(Y2~P!1).S(NSH2~O!1,CSH2,PTP~O) <-> R(Y1~P!2).R(Y2~P!1).S(NSH2~O!1,CSH2,PTP~O!2)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="2", bond_type="radded")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        EndWhiteSpace(),
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="1")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="2", bond_type="radded")))),
    )
)

add("R(Y1~P,Y2~P!1).S(NSH2~O!1,CSH2,PTP~O) <-> R(Y1~P!2,Y2~P!1).S(NSH2~O!1,CSH2,PTP~O!2)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="2", bond_type="radded")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="1")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="2", bond_type="radded")))),
    )
)

add("R(Y1~P!1,Y2~P).S(NSH2~O,CSH2,PTP~O!1) <-> R(Y1~P!1,Y2~P!2).S(NSH2~O,CSH2!2,PTP~O!1)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="2", bond_type="radded")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bond_num="2", bond_type="radded")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="1")))),
    )
)

add("R(Y1~P!1).R(Y2~P).S(NSH2~O,CSH2,PTP~O!1) <-> R(Y1~P!1).R(Y2~P!2).S(NSH2~O,CSH2!2,PTP~O!1)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        EndWhiteSpace(),
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="2", bond_type="radded")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bond_num="2", bond_type="radded")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="1")))),
    )
)

add("R(Y1~P!1).R(Y2~P).S(NSH2~O,CSH2,PTP~O!1) <-> R(Y1~P!1).R(Y2~P!2).S(NSH2~O!2,CSH2,PTP~O!1)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        EndWhiteSpace(),
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="2", bond_type="radded")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="2", bond_type="radded")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="1")))),
    )
)

add("R(Y1~P!1,Y2~P).S(NSH2~O,CSH2,PTP~O!1) <-> R(Y1~P!1,Y2~P!2).S(NSH2~O!2,CSH2,PTP~O!1)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="2", bond_type="radded")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="2", bond_type="radded")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="1")))),
    )
)

add("R(Y1~P,Y2~P!1).R(Y2~P!2).S(NSH2~O!2,CSH2!1,PTP~O) <-> R(Y1~P!3,Y2~P!1).R(Y2~P!2).S(NSH2~O!2,CSH2!1,PTP~O!3)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="3", bond_type="radded")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1")))),
        EndWhiteSpace(),
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="2")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="2")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bond_num="1")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="3", bond_type="radded")))),
    )
)

add("R(Y1~P,Y2~P!1).R(Y2~P!2).S(NSH2~O!1,CSH2!2,PTP~O) <-> R(Y1~P!3,Y2~P!1).R(Y2~P!2).S(NSH2~O!1,CSH2!2,PTP~O!3)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="3", bond_type="radded")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1")))),
        EndWhiteSpace(),
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="2")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="1")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bond_num="2")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="3", bond_type="radded")))),
    )
)

add("R(Y1~P!1,Y2~P!2).R(Y2~P).S(NSH2~O,CSH2!2,PTP~O!1) <-> R(Y1~P!1,Y2~P!2).R(Y2~P!3).S(NSH2~O!3,CSH2!2,PTP~O!1)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="2")))),
        EndWhiteSpace(),
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="3", bond_type="radded")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="3", bond_type="radded")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bond_num="2")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="1")))),
    )
)

add("R(Y2~P!1).R(Y1~P!2,Y2~P).S(NSH2~O,CSH2!1,PTP~O!2) <-> R(Y2~P!1).R(Y1~P!2,Y2~P!3).S(NSH2~O!3,CSH2!1,PTP~O!2)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1")))),
        EndWhiteSpace(),
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="2")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="3", bond_type="radded")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="3", bond_type="radded")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bond_num="1")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="2")))),
    )
)

add("R(Y2~P!1).R(Y1~P!2,Y2~P).S(NSH2~O!1,CSH2,PTP~O!2) <-> R(Y2~P!1).R(Y1~P!2,Y2~P!3).S(NSH2~O!1,CSH2!3,PTP~O!2)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1")))),
        EndWhiteSpace(),
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="2")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="3", bond_type="radded")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="1")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bond_num="3", bond_type="radded")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="2")))),
    )
)

add("R(Y1~P!1,Y2~P!2).R(Y2~P).S(NSH2~O!2,CSH2,PTP~O!1) <-> R(Y1~P!1,Y2~P!2).R(Y2~P!3).S(NSH2~O!2,CSH2!3,PTP~O!1)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="1")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="2")))),
        EndWhiteSpace(),
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("U", box_color="khaki"), NonTerminal("P", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bond_num="3", bond_type="radded")))),
        EndWhiteSpace(),
        Terminal("S", box_color="lightgreen"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="2")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightblue', bottom_bind=True, bond_num="3", bond_type="radded")),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("O", box_color="khaki", bottom_bind=True, bond_num="1")))),
    )
)
