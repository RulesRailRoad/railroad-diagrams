
add("EGFR(ecd,tmd,y1068~u~p,y1173~u~p)",
    Diagram(Terminal("EGFR", box_color="lightblue"),
    Choice(0, Comment("    "), Terminal("ecd", box_color='lightgreen')),
    Choice(0, Comment("    "), Terminal("tmd", box_color='lightgreen')),
    Choice(0, Comment("    "), Sequence(Terminal("y1068", box_color='lightgreen'), Choice(0, Comment("    "), NonTerminal("~u", box_color="yellow"), NonTerminal("~p", box_color="yellow")))),
    Choice(0, Comment("    "), Sequence(Terminal("y1173", box_color='lightgreen'), Choice(0, Comment("    "), NonTerminal("~u", box_color="yellow"), NonTerminal("~p", box_color="yellow")))),
   )
)

add("EGF(rb)",
    Diagram(Terminal("EGF", box_color="lightblue"),
    Choice(0, Comment("    "), Terminal("rb", box_color='lightgreen')),
   )
)

add("Grb2(sh2,sos)",
    Diagram(Terminal("Grb2", box_color="lightblue"),
    Choice(0, Comment("    "), Terminal("sh2", box_color='lightgreen')),
    Choice(0, Comment("    "), Terminal("sos", box_color='lightgreen')),
   )
)

add("Shc(sh3,Y773~p~u)",
    Diagram(Terminal("Shc", box_color="lightblue"),
    Choice(0, Comment("    "), Terminal("sh3", box_color='lightgreen')),
    Choice(0, Comment("    "), Sequence(Terminal("Y773", box_color='lightgreen'), Choice(0, Comment("    "), NonTerminal("~p", box_color="yellow"), NonTerminal("~u", box_color="yellow")))),
   )
)
