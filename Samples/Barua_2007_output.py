
add("R(DD,Y1~U~P,Y2~P)",
    Diagram(Terminal("R", box_color="lightblue"),
    Choice(0, Comment("    "), Terminal("DD", box_color='lightgreen')),
    Choice(0, Comment("    "), Sequence(Terminal("Y1", box_color='lightgreen'), Choice(0, Comment("    "), NonTerminal("~U", box_color="yellow"), NonTerminal("~P", box_color="yellow")))),
    Choice(0, Comment("    "), Sequence(Terminal("Y2", box_color='lightgreen'), Choice(0, Comment("    "), NonTerminal("~P", box_color="yellow")))),
   )
)

add("S(NSH2~C~O,CSH2,PTP~C~O)",
    Diagram(Terminal("S", box_color="lightblue"),
    Choice(0, Comment("    "), Sequence(Terminal("NSH2", box_color='lightgreen'), Choice(0, Comment("    "), NonTerminal("~C", box_color="yellow"), NonTerminal("~O", box_color="yellow")))),
    Choice(0, Comment("    "), Terminal("CSH2", box_color='lightgreen')),
    Choice(0, Comment("    "), Sequence(Terminal("PTP", box_color='lightgreen'), Choice(0, Comment("    "), NonTerminal("~C", box_color="yellow"), NonTerminal("~O", box_color="yellow")))),
   )
)
