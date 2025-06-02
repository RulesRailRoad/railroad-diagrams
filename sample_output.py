sys.stdout.write("<h1>Molecules</h1>\n")


add("egf(r)",
    Diagram(
      Terminal("egf", box_color="orange"),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen")),
    )
)

add("egfr(l,r,Y1068~Y~pY,Y1148~Y~pY)",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen")),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow")))),
    )
)

add("Shc(PTB,Y317~Y~pY)",
    Diagram(
      Terminal("Shc", box_color="orange"),
        Choice(0, Comment("    "), Terminal("PTB", box_color="lightgreen")),
        Choice(0, Comment("    "), Sequence(Terminal("Y317", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow")))),
    )
)

add("Grb2(SH2,SH3)",
    Diagram(
      Terminal("Grb2", box_color="orange"),
        Choice(0, Comment("    "), Terminal("SH2", box_color="lightgreen")),
        Choice(0, Comment("    "), Terminal("SH3", box_color="lightgreen")),
    )
)

add("Sos(dom)",
    Diagram(
      Terminal("Sos", box_color="orange"),
        Choice(0, Comment("    "), Terminal("dom", box_color="lightgreen")),
    )
)
sys.stdout.write("<h1>Species</h1>\n")


add("egf(r)",
    Diagram(
      Terminal("egf", box_color="orange"),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen")),
    )
)

add("Grb2(SH2,SH3)",
    Diagram(
      Terminal("Grb2", box_color="orange"),
        Choice(0, Comment("    "), Terminal("SH2", box_color="lightgreen")),
        Choice(0, Comment("    "), Terminal("SH3", box_color="lightgreen")),
    )
)

add("Shc(PTB,Y317~Y)",
    Diagram(
      Terminal("Shc", box_color="orange"),
        Choice(0, Comment("    "), Terminal("PTB", box_color="lightgreen")),
        Choice(0, Comment("    "), Sequence(Terminal("Y317", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow")))),
    )
)

add("Sos(dom)",
    Diagram(
      Terminal("Sos", box_color="orange"),
        Choice(0, Comment("    "), Terminal("dom", box_color="lightgreen")),
    )
)

add("egfr(l,r,Y1068~Y,Y1148~Y)",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen")),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow")))),
    )
)

add("Grb2(SH2,SH3!1).Sos(dom!1)",
    Diagram(
      Terminal("Grb2", box_color="orange"),
        Choice(0, Comment("    "), Terminal("SH2", box_color="lightgreen")),
        Choice(0, Comment("    "), Terminal("SH3", box_color="lightgreen", bottom_bind=True, bond_num="1")),
        EndWhiteSpace(),
      Terminal("Sos", box_color="orange"),
        Choice(0, Comment("    "), Terminal("dom", box_color="lightgreen", bottom_bind=True, bond_num="1")),
    )
)
sys.stdout.write("<h1>Observables</h1>\n")


add("egfr(l!?,r!?,Y1068~Y~pY!?,Y1148~Y~pY!?).egfr(l!?,r!?,Y1068~Y~pY!?,Y1148~Y~pY!?)",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        EndWhiteSpace(),
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
    )
)

add("Shc(PTB!+,Y317~pY!2).Grb2(SH2!2,SH3!3).Sos(dom!3)",
    Diagram(
      Terminal("Shc", box_color="orange"),
        Choice(0, Comment("    "), Terminal("PTB", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Sequence(Terminal("Y317", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("pY", box_color="yellow", bottom_bind=True, bond_num="2")))),
        EndWhiteSpace(),
      Terminal("Grb2", box_color="orange"),
        Choice(0, Comment("    "), Terminal("SH2", box_color="lightgreen", bottom_bind=True, bond_num="2")),
        Choice(0, Comment("    "), Terminal("SH3", box_color="lightgreen", bottom_bind=True, bond_num="3")),
        EndWhiteSpace(),
      Terminal("Sos", box_color="orange"),
        Choice(0, Comment("    "), Terminal("dom", box_color="lightgreen", bottom_bind=True, bond_num="3")),
    )
)

add("egfr(l!?,r!?,Y1068~Y~pY!?,Y1148~pY!?)",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
    )
)

add("egfr(l!?,r!?,Y1068~Y~pY!?,Y1148~Y~pY!?)",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
    )
)
sys.stdout.write("<h1>Reactions</h1>\n")


add("egfr(l!-,r!-,Y1068~Y~pY!?,Y1148~Y~pY!?)   + egf(r!-)",
    Diagram(
              Terminal("egfr", box_color="orange"),
                Choice(0, Comment("    "), Terminal("l", box_color="lightgreen")),
                Choice(0, Comment("    "), Terminal("r", box_color="lightgreen")),
                Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
                Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
                EndWhiteSpace(),
              Terminal("egf", box_color="orange"),
                Choice(0, Comment("    "), Terminal("r", box_color="lightgreen"))
    )
)

add("egfr(l!1,r!-,Y1068~Y~pY!?,Y1148~Y~pY!?).egf(r!1)  kp1, km1   #ligand-monomer",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True, bond_num="1", bond_type='radded')),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen")),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        EndWhiteSpace(),
      Terminal("egf", box_color="orange"),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True, bond_num="1", bond_type='radded')),
    )
)

add("egfr(l!+,r!-,Y1068~Y~pY!?,Y1148~Y~pY!?) + egfr(l!+,r!-,Y1068~Y~pY!?,Y1148~Y~pY!?)",
    Diagram(
              Terminal("egfr", box_color="orange"),
                Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True)),
                Choice(0, Comment("    "), Terminal("r", box_color="lightgreen")),
                Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
                Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
                EndWhiteSpace(),
              Terminal("egfr", box_color="orange"),
                Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True)),
                Choice(0, Comment("    "), Terminal("r", box_color="lightgreen")),
                Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
                Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?"))))
    )
)

add("egfr(l!+,r!3,Y1068~Y~pY!?,Y1148~Y~pY!?).egfr(l!+,r!3,Y1068~Y~pY!?,Y1148~Y~pY!?)  kp2,km2",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True, bond_num="3", bond_type='diamond')),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        EndWhiteSpace(),
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True, bond_num="3", bond_type='diamond')),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
    )
)

add("egfr(l!?, r!+,Y1068~Y!-, Y1148~Y~pY!?)",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
    )
)

add("egfr(l!?, r!+,Y1068~pY!-, Y1148~Y~pY!?)  kp3",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("pY", box_color="yellow")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
    )
)

add("egfr(l!?, r!+,Y1068~Y~pY!?, Y1148~Y!-)",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow")))),
    )
)

add("egfr(l!?, r!+,Y1068~Y~pY!?, Y1148~pY!-)  kp3",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("pY", box_color="yellow")))),
    )
)

add("egfr(l!?, r!+,Y1068~pY!-, Y1148~Y~pY!?)",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("pY", box_color="yellow")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
    )
)

add("egfr(l!?, r!+,Y1068~Y!-, Y1148~Y~pY!?)  km3",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
    )
)

add("egfr(l!?, r!+,Y1068~Y~pY!?, Y1148~pY!-)",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("pY", box_color="yellow")))),
    )
)

add("egfr(l!?, r!+,Y1068~Y~pY!?, Y1148~Y!-)  km3",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow")))),
    )
)

add("egfr(l!?,r!+,Y1068~Y~pY!?,Y1148~pY!1).Shc(PTB!1,Y317~Y!-)",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("pY", box_color="yellow", bottom_bind=True, bond_num="1")))),
        EndWhiteSpace(),
      Terminal("Shc", box_color="orange"),
        Choice(0, Comment("    "), Terminal("PTB", box_color="lightgreen", bottom_bind=True, bond_num="1")),
        Choice(0, Comment("    "), Sequence(Terminal("Y317", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow")))),
    )
)

add("egfr(l!?,r!+,Y1068~Y~pY!?,Y1148~pY!1).Shc(PTB!1,Y317~pY!-)  kp14",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow", bottom_bind=True, bottom_bind_color="gray", bond_num="?")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("pY", box_color="yellow", bottom_bind=True, bond_num="1")))),
        EndWhiteSpace(),
      Terminal("Shc", box_color="orange"),
        Choice(0, Comment("    "), Terminal("PTB", box_color="lightgreen", bottom_bind=True, bond_num="1")),
        Choice(0, Comment("    "), Sequence(Terminal("Y317", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("pY", box_color="yellow")))),
    )
)

add("Shc(PTB!+,Y317~pY!-)",
    Diagram(
      Terminal("Shc", box_color="orange"),
        Choice(0, Comment("    "), Terminal("PTB", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Sequence(Terminal("Y317", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("pY", box_color="yellow")))),
    )
)

add("Shc(PTB!+,Y317~Y!-)  km14",
    Diagram(
      Terminal("Shc", box_color="orange"),
        Choice(0, Comment("    "), Terminal("PTB", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Sequence(Terminal("Y317", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow")))),
    )
)


add("Shc(PTB!+,Y317~pY!-)  ->  Shc(PTB!+,Y317~Y!-)",
    Diagram(
      Terminal("Shc", box_color="orange"),
        Choice(0, Comment("    "), Terminal("PTB", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Sequence(Terminal("Y317", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("Y", box_color="green"), NonTerminal("pY", box_color="red")))),
    )
)

add("Shc(PTB!+,Y317~pY!-)  ->  Shc(PTB!+,Y317~Y!-)",
    Diagram(
      Terminal("Shc", box_color="orange"),
        Choice(0, Comment("    "), Terminal("PTB", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Sequence(Terminal("Y317", box_color="lightgreen"), Choice(0, Comment('    '), MultipleChoice(0, 'any', NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow"))))),
    )
)

add('test',
    Diagram(
Sequence(
    Terminal("Y1148", box_color="lightgreen", bottom_bind = True, wrap=True),  # No bond here
    Choice(
        0, Comment(" "),
        NonTerminal("Y", box_color="yellow"), 
        NonTerminal("pY", box_color="yellow")
    )
)
    ))




add("egfr(l!?,r!+,Y1068~Y~pY!?,Y1148~pY!1).Shc(PTB!1,Y317~Y!-) -> egfr(l!?,r!+,Y1068~Y~pY!?,Y1148~pY!1).Shc(PTB!1,Y317~pY!-)",
    Diagram(
      Terminal("egfr", box_color="orange"),
        Choice(0, Comment("    "), Terminal("l", box_color="lightgreen", bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        Choice(0, Comment("    "), Terminal("r", box_color="lightgreen", bottom_bind=True)),
        Choice(0, Comment("    "), Sequence(Terminal("Y1068", box_color="lightgreen", bottom_bind=True, wrap=True), Choice(0, Comment("    "), NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow")))),
        Choice(0, Comment("    "), Sequence(Terminal("Y1148", box_color="lightgreen"), Choice(0, Comment("    "), NonTerminal("pY", box_color="yellow", bottom_bind=True, bond_num="1")))),
        EndWhiteSpace(),
      Terminal("Shc", box_color="orange"),
        Choice(0, Comment("    "), Terminal("PTB", box_color="lightgreen", bottom_bind=True, bond_num="1")),
        Choice(0, Comment("    "), Sequence(Terminal("Y317", box_color="lightgreen"), Choice(0, Comment("    "), MultipleChoice(0, 'all', NonTerminal("Y", box_color="yellow"), NonTerminal("pY", box_color="yellow"))))),
    )
)