sys.stdout.write("<h1>Molecules</h1>\n")


add("egf(r)",
    Diagram(
        Terminal("egf", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue')),
    )
)

add("egfr(l,r,Y1068~Y~pY,Y1148~Y~pY)",
    Diagram(
        Terminal("egfr", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("l", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki")))),
    )
)

add("Shc(PTB,Y317~Y~pY)",
    Diagram(
        Terminal("Shc", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("PTB", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("Y317", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki")))),
    )
)

add("Grb2(SH2,SH3)",
    Diagram(
        Terminal("Grb2", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("SH2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("SH3", box_color='lightblue')),
    )
)

add("Sos(dom)",
    Diagram(
        Terminal("Sos", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("dom", box_color='lightblue')),
    )
)
sys.stdout.write("<h1>Species</h1>\n")


add("egf(r)",
    Diagram(
        Terminal("egf", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue')),
    )
)

add("Grb2(SH2,SH3)",
    Diagram(
        Terminal("Grb2", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("SH2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("SH3", box_color='lightblue')),
    )
)

add("Shc(PTB,Y317~Y)",
    Diagram(
        Terminal("Shc", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("PTB", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("Y317", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki")))),
    )
)

add("Sos(dom)",
    Diagram(
        Terminal("Sos", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("dom", box_color='lightblue')),
    )
)

add("egfr(l,r,Y1068~Y,Y1148~Y)",
    Diagram(
        Terminal("egfr", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("l", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki")))),
    )
)

add("Grb2(SH2,SH3!1).Sos(dom!1)",
    Diagram(
        Terminal("Grb2", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("SH2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("SH3", box_color='lightblue', bottom_bind=True, bond_num="1")),
        EndWhiteSpace(),
        Terminal("Sos", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("dom", box_color='lightblue', bottom_bind=True, bond_num="1")),
    )
)
sys.stdout.write("<h1>Observables</h1>\n")


add("egfr(l!?,r!?,Y1068~Y~pY!?,Y1148~Y~pY!?).egfr(l!?,r!?,Y1068~Y~pY!?,Y1148~Y~pY!?)",
    Diagram(
        Terminal("egfr", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("l", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
        EndWhiteSpace(),
        Terminal("egfr", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("l", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)

add("Shc(PTB!+,Y317~pY!2).Grb2(SH2!2,SH3!3).Sos(dom!3), egfr(Y1068~pY!1).Grb2(SH2!1,SH3!2).Sos(dom!2)",
    Diagram(
        Terminal("Shc", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("PTB", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Sequence(Terminal("Y317", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("pY", box_color="khaki", bottom_bind=True, bond_num="2")))),
        EndWhiteSpace(),
        Terminal("Grb2", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("SH2", box_color='lightblue', bottom_bind=True, bond_num="2")),
    Choice(0, Comment("    "), Terminal("SH3", box_color='lightblue', bottom_bind=True, bond_num="3")),
        EndWhiteSpace(),
        Terminal("Sos", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("dom", box_color='lightblue', bottom_bind=True, bond_num="3")),
        EndWhiteSpace(),
        Terminal("Grb2", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("SH2", box_color='lightblue', bottom_bind=True, bond_num="1")),
    Choice(0, Comment("    "), Terminal("SH3", box_color='lightblue', bottom_bind=True, bond_num="2")),
        EndWhiteSpace(),
        Terminal("Sos", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("dom", box_color='lightblue', bottom_bind=True, bond_num="2")),
    )
)

add("egfr(l!?,r!?,Y1068~Y~pY!?,Y1148~pY!?), egfr(l!?,r!?,Y1068~pY!?,Y1148~Y~pY!?)",
    Diagram(
        Terminal("egfr", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("l", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("pY", box_color="khaki", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
    )
)

add("egfr(l!?,r!?,Y1068~Y~pY!?,Y1148~Y~pY!?)",
    Diagram(
        Terminal("egfr", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("l", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)
sys.stdout.write("<h1>Reactions</h1>\n")


add("egfr(l!-,r!-,Y1068~Y~pY!?,Y1148~Y~pY!?) + egf(r!-) <-> egfr(l!1,r!-,Y1068~Y~pY!?,Y1148~Y~pY!?).egf(r!1)",
    Diagram(
        Terminal("egfr", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("l", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue')),
    Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
        EndWhiteSpace(),
        Terminal("egf", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    )
)

add("egfr(l!+,r!-,Y1068~Y~pY!?,Y1148~Y~pY!?) + egfr(l!+,r!-,Y1068~Y~pY!?,Y1148~Y~pY!?) <-> egfr(l!+,r!3,Y1068~Y~pY!?,Y1148~Y~pY!?).egfr(l!+,r!3,Y1068~Y~pY!?,Y1148~Y~pY!?)",
    Diagram(
        Terminal("egfr", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("l", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue', bottom_bind=True, bond_num="3", bond_type="radded")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
        EndWhiteSpace(),
        Terminal("egfr", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("l", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue', bottom_bind=True, bond_num="3", bond_type="radded")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)

add("egfr(l!+,r!-,Y1068~Y!?,Y1148~Y~pY!?) + egfr(l!+,r!-,Y1068~Y~pY!?,Y1148~Y~pY!?) <-> egfr(l!+,r!3,Y1068~pY!?,Y1148~Y~pY!?).egfr(l!+,r!3,Y1068~Y~pY!?,Y1148~Y~pY!?)",
    Diagram(
        Terminal("egfr", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("l", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue', bottom_bind=True, bond_num="3", bond_type="radded")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("Y", box_color="khaki", bottom_bind=True, bottom_bind_color="gray", bond_num="?"), NonTerminal("pY", box_color="khaki"))))),
    Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
        EndWhiteSpace(),
        Terminal("egfr", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("l", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue', bottom_bind=True, bond_num="3", bond_type="radded")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)

add("egfr(l!?, r!+,Y1068~Y!-, Y1148~Y~pY!?) -> egfr(l!?, r!+,Y1068~pY!-, Y1148~Y~pY!?)",
    Diagram(
        Terminal("egfr", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("l", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki"))))),
    Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)

add("egfr(l!?, r!+,Y1068~Y~pY!?, Y1148~Y!-) -> egfr(l!?, r!+,Y1068~Y~pY!?, Y1148~pY!-)",
    Diagram(
        Terminal("egfr", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("l", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki"))))),
    )
)

add("egfr(l!?, r!+,Y1068~pY!-, Y1148~Y~pY!?) -> egfr(l!?, r!+,Y1068~Y!-, Y1148~Y~pY!?)",
    Diagram(
        Terminal("egfr", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("l", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "up-arrow", NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki"))))),
    Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    )
)

add("egfr(l!?, r!+,Y1068~Y~pY!?, Y1148~pY!-) -> egfr(l!?, r!+,Y1068~Y~pY!?, Y1148~Y!-)",
    Diagram(
        Terminal("egfr", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("l", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "up-arrow", NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki"))))),
    )
)

add("egfr(l!?,r!+,Y1068~Y~pY!?,Y1148~pY!1).Shc(PTB!1,Y317~Y!-) -> egfr(l!?,r!+,Y1068~Y~pY!?,Y1148~pY!1).Shc(PTB!1,Y317~pY!-)",
    Diagram(
        Terminal("egfr", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("l", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("r", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki", bottom_bind=True, wrap=True)))),
    Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color='lightblue'), Choice(0, Comment("    "), NonTerminal("pY", box_color="khaki", bottom_bind=True, bond_num="1")))),
        EndWhiteSpace(),
        Terminal("Shc", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("PTB", box_color='lightblue', bottom_bind=True, bond_num="1")),
    Choice(0, Comment("    "), Sequence(Terminal("Y317", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "down-arrow", NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki"))))),
    )
)

add("Shc(PTB!+,Y317~pY!-) -> Shc(PTB!+,Y317~Y!-)",
    Diagram(
        Terminal("Shc", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("PTB", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Sequence(Terminal("Y317", box_color='lightblue'), Choice(0, Comment("    "), MultipleChoice(0, "up-arrow", NonTerminal("Y", box_color="khaki"), NonTerminal("pY", box_color="khaki"))))),
    )
)
