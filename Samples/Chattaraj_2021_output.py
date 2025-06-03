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


add("Nck(S1,S2,S3,Sh2)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue')),
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

add("Nephrin(pY1,pY2,pY3)",
    Diagram(
        Terminal("Nephrin", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("pY1", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("pY2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("pY3", box_color='lightblue')),
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

add("Nephrin(pY1,pY2,pY3).Nck(S1,S2,S3,Sh2).NWASP(p1,p2,p3,p4,p5,p6)",
    Diagram(
        Terminal("Nephrin", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("pY1", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("pY2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("pY3", box_color='lightblue')),
        EndWhiteSpace(),
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue')),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue')),
    )
)

add("Nck(S1,S2,S3,Sh2).NWASP(p1,p2,p3,p4,p5,p6)",
    Diagram(
        Terminal("Nck", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightblue')),
        EndWhiteSpace(),
        Terminal("NWASP", box_color="lightgreen"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightblue')),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightblue')),
    )
)
