
add("Nephrin(pY1,pY2,pY3)",
    Diagram(Terminal("Nephrin", box_color="lightblue"),
    Choice(0, Comment("    "), Terminal("pY1", box_color='lightgreen')),
    Choice(0, Comment("    "), Terminal("pY2", box_color='lightgreen')),
    Choice(0, Comment("    "), Terminal("pY3", box_color='lightgreen')),
   )
)

add("Nck(S1,S2,S3,Sh2)",
    Diagram(Terminal("Nck", box_color="lightblue"),
    Choice(0, Comment("    "), Terminal("S1", box_color='lightgreen')),
    Choice(0, Comment("    "), Terminal("S2", box_color='lightgreen')),
    Choice(0, Comment("    "), Terminal("S3", box_color='lightgreen')),
    Choice(0, Comment("    "), Terminal("Sh2", box_color='lightgreen')),
   )
)

add("NWASP(p1,p2,p3,p4,p5,p6)",
    Diagram(Terminal("NWASP", box_color="lightblue"),
    Choice(0, Comment("    "), Terminal("p1", box_color='lightgreen')),
    Choice(0, Comment("    "), Terminal("p2", box_color='lightgreen')),
    Choice(0, Comment("    "), Terminal("p3", box_color='lightgreen')),
    Choice(0, Comment("    "), Terminal("p4", box_color='lightgreen')),
    Choice(0, Comment("    "), Terminal("p5", box_color='lightgreen')),
    Choice(0, Comment("    "), Terminal("p6", box_color='lightgreen')),
   )
)
