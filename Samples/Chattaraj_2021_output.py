sys.stdout.write("<h1>Molecules</h1>\n")


add("Nephrin(pY1,pY2,pY3)",
    Diagram(
        Terminal("Nephrin", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("pY1", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("pY2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("pY3", box_color='lightblue')),
    )
)

add("Nck(S1,S2,S3,Sh2)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue')),
    )
)

add("NWASP(p1,p2,p3,p4,p5,p6)",
    Diagram(
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue')),
    )
)
sys.stdout.write("<h1>Species</h1>\n")


add("Nephrin(pY1,pY2,pY3)",
    Diagram(
        Terminal("Nephrin", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("pY1", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("pY2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("pY3", box_color='lightblue')),
    )
)

add("Nck(S1,S2,S3,Sh2)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue')),
    )
)

add("NWASP(p1,p2,p3,p4,p5,p6)",
    Diagram(
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue')),
    )
)
sys.stdout.write("<h1>Observables</h1>\n")


add("Nck()",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck(S1,S2,S3,Sh2)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue')),
    )
)

add("NWASP()",
    Diagram(
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("NWASP(p1,p2,p3,p4,p5,p6)",
    Diagram(
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue')),
    )
)

add("Nephrin()",
    Diagram(
        Terminal("Nephrin", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("pY1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("pY2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("pY3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nephrin(pY1,pY2,pY3)",
    Diagram(
        Terminal("Nephrin", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("pY1", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("pY2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("pY3", box_color='lightblue')),
    )
)

add("Nephrin(pY1!+,pY2!+,pY3!+)",
    Diagram(
        Terminal("Nephrin", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("pY1", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Terminal("pY2", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Terminal("pY3", box_color='lightblue', bottom_bind=True, bond_num="+")),
    )
)

add("Nck(S1!+,S2!+,S3!+,Sh2!+)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bond_num="+")),
    )
)

add("NWASP(p1!+,p2!+,p3!+,p4!+,p5!+,p6!+)",
    Diagram(
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bond_num="+")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bond_num="+")),
    )
)

add("Nephrin().Nck().NWASP()",
    Diagram(
        Terminal("Nephrin", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("pY1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("pY2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("pY3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck().NWASP()",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)
sys.stdout.write("<h1>Reactions</h1>\n")


add("Nck(S1) + NWASP(p1) <-> Nck(S1!1).NWASP(p1!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck(S2) + NWASP(p1) <-> Nck(S2!1).NWASP(p1!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck(S3) + NWASP(p1) <-> Nck(S3!1).NWASP(p1!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck(S3) + NWASP(p2) <-> Nck(S3!1).NWASP(p2!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck(S2) + NWASP(p2) <-> Nck(S2!1).NWASP(p2!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck(S1) + NWASP(p2) <-> Nck(S1!1).NWASP(p2!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck(S2) + NWASP(p3) <-> Nck(S2!1).NWASP(p3!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck(S1) + NWASP(p3) <-> Nck(S1!1).NWASP(p3!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck(S3) + NWASP(p3) <-> Nck(S3!1).NWASP(p3!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck(S1) + NWASP(p4) <-> Nck(S1!1).NWASP(p4!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck(S2) + NWASP(p4) <-> Nck(S2!1).NWASP(p4!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck(S3) + NWASP(p4) <-> Nck(S3!1).NWASP(p4!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck(S1) + NWASP(p5) <-> Nck(S1!1).NWASP(p5!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck(S2) + NWASP(p5) <-> Nck(S2!1).NWASP(p5!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck(S3) + NWASP(p5) <-> Nck(S3!1).NWASP(p5!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    )
)

add("Nck(S1) + NWASP(p6) <-> Nck(S1!1).NWASP(p6!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    )
)

add("Nck(S3) + NWASP(p6) <-> Nck(S3!1).NWASP(p6!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    )
)

add("Nck(S2) + NWASP(p6) <-> Nck(S2!1).NWASP(p6!1)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    )
)

add("Nephrin(pY1) + Nck(Sh2) <-> Nephrin(pY1!1).Nck(Sh2!1)",
    Diagram(
        Terminal("Nephrin", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("pY1", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("pY2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("pY3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    )
)

add("Nephrin(pY2) + Nck(Sh2) <-> Nephrin(pY2!1).Nck(Sh2!1)",
    Diagram(
        Terminal("Nephrin", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("pY1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("pY2", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    Choice(0, Comment("    "), Terminal("pY3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
        EndWhiteSpace(),
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    )
)

add("Nephrin(pY3) + Nck(Sh2) <-> Nephrin(pY3!1).Nck(Sh2!1)",
    Diagram(
        Terminal("Nephrin", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("pY1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("pY2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("pY3", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
        EndWhiteSpace(),
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue', bottom_bind=True, bottom_bind_color="gray", bond_num="?")),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue', bottom_bind=True, bond_num="1", bond_type="radded")),
    )
)
