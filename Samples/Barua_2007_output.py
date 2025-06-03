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
        EndWhiteSpace(),
    )
)
sys.stdout.write("<h1>Observables</h1>\n")


add("R(DD,Y1~P!?,Y2~P)",
    Diagram(
        Terminal("R", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("P", box_color="khaki")))),
    )
)
