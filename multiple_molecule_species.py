# diagrams for species with multiple molecules

add('Option1: A(site1!1).B(site1!1)',
    Diagram(
        'A(',
        Choice(0, Comment("                    "), 
               Sequence('site1',
                    Choice(0, Comment("    "), '!1'),)
               ),

        ')',

        '.',

        'B(',
        Choice(0, Comment("                    "), 
               Sequence('site1',
                       Choice(0, Comment("    "), '!1'),)
                 ),
        ')'
    ))


add('Option2: A(site1!1).B(site1!1)',
    Diagram(
        Stack(
           Sequence('A(',
                Choice(0, Comment("                    "), 
            Sequence('site1',
                Choice(0, Comment("    "), '!1'),)
            ),

        ')',
        '.',
            ),

            Sequence('B(',
                Choice(0, Comment("                    "), 
            Sequence('site1',
                Choice(0, Comment("    "), '!1'),)
            ),
        ')'
            ))

))


add('Option1: A(site1~U!1).B(site1~P!1)',
    Diagram(
   'A(',
   Choice(0, Comment("                                "), 
         Sequence('site1',
              Choice(0, Comment("                "), Sequence('~U', Choice(0, Comment('    '), '!1')),

               ))),

        ')',

        '.',
        
        'B(',
        Choice(0, Comment("                                "), 
               Sequence('site1',
                       Choice(0, Comment("                "), Sequence('~P', Choice(0, Comment('    '), '!1')) ),)
                 ),
        ')'

    ))


add('Option2: A(site1~U!1).B(site1~P!1)',
    Diagram(
        Stack(
            Sequence(
            'A(',
                Choice(0, Comment("                                "), 
                    Sequence('site1',
                Choice(0, Comment("                "), Sequence('~U', Choice(0, Comment('    '), '!1')),

               ))),

        ')',

        '.',
),
            Sequence(
            'B(',
                Choice(0, Comment("                                "), 
                    Sequence('site1',
                Choice(0, Comment("                "), Sequence('~P', Choice(0, Comment('    '), '!1')) ),)
                 ),
        ')'
)

    )
))


# BNGL to Python molecules
add('EGFR(ecd,tmd,y1068~u~p,y1173~u~p)',
Diagram("EGFR(",
    Choice(0, Comment("                "), "ecd"),
    Choice(0, Comment("                "), "tmd"),
    Choice(0, Comment("              "), Sequence("y1068", Choice(0, Comment("            "), "~u", "~p"))),
    Choice(0, Comment("              "), Sequence("y1173", Choice(0, Comment("            "), "~u", "~p"))),
    ")"
))
add('MAP3K(s, S~I~A)',
Diagram("MAP3K(",
    Choice(0, Comment("                "), "s"),
    Choice(0, Comment("              "), Sequence("S", Choice(0, Comment("            "), "~I", "~A"))),
    ")"
))
add('Grb2(sh2,sos)',
Diagram("Grb2(",
    Choice(0, Comment("                "), "sh2"),
    Choice(0, Comment("                "), "sos"),
    ")"
))
add('Shc(sh3,Y773~p~u)',
Diagram("Shc(",
    Choice(0, Comment("                "), "sh3"),
    Choice(0, Comment("              "), Sequence("Y773", Choice(0, Comment("            "), "~p", "~u"))),
    ")"
))
add('C(site,Y1~u~p,Y2~u~p,Y3~u~p)',
Diagram("C(",
    Choice(0, Comment("                "), "site"),
    Choice(0, Comment("              "), Sequence("Y1", Choice(0, Comment("            "), "~u", "~p"))),
    Choice(0, Comment("              "), Sequence("Y2", Choice(0, Comment("            "), "~u", "~p"))),
    Choice(0, Comment("              "), Sequence("Y3", Choice(0, Comment("            "), "~u", "~p"))),
    ")"
))
add('S(E~0~1,F~0~1,A~0~1,Y~U~P~2P~3P~4P~5P~6P~7P~8P~9P~10P~11P~12P~13P~14P~15P~16P~17P~18P~19P~20P)',
Diagram("S(",
    Choice(0, Comment("              "), Sequence("E", Choice(0, Comment("            "), "~0", "~1"))),
    Choice(0, Comment("              "), Sequence("F", Choice(0, Comment("            "), "~0", "~1"))),
    Choice(0, Comment("              "), Sequence("A", Choice(0, Comment("            "), "~0", "~1"))),
    Choice(0, Comment("              "), Sequence("Y", Choice(0, Comment("            "), "~U", "~P", "~2P", "~3P", "~4P", "~5P", "~6P", "~7P", "~8P", "~9P", "~10P", "~11P", "~12P", "~13P", "~14P", "~15P", "~16P", "~17P", "~18P", "~19P", "~20P"))),
    ")"
))
add('ErbB3(I_III,II,Y1054~O~P,Y1197~O~P,Y1222~O~P,Y1260~O~P,Y1276~O~P,Y1289~O~P,Y1328~O~P,loc~M~En)',
Diagram("ErbB3(",
    Choice(0, Comment("                "), "I_III"),
    Choice(0, Comment("                "), "II"),
    Choice(0, Comment("              "), Sequence("Y1054", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("Y1197", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("Y1222", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("Y1260", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("Y1276", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("Y1289", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("Y1328", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("loc", Choice(0, Comment("            "), "~M", "~En"))),
    ")"
))
add('Raf1(RBD,STkinase,S29~O~P,S43~O~P,S259~O~P,S289~O~P,S296~O~P,S301~O~P,S338~O~P,Y341~O~P,S471~O~P,T491~O~P,S494~O~P,S642~O~P,loc~C)',
Diagram("Raf1(",
    Choice(0, Comment("                "), "RBD"),
    Choice(0, Comment("                "), "STkinase"),
    Choice(0, Comment("              "), Sequence("S29", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("S43", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("S259", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("S289", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("S296", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("S301", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("S338", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("Y341", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("S471", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("T491", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("S494", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("S642", Choice(0, Comment("            "), "~O", "~P"))),
    Choice(0, Comment("              "), Sequence("loc", Choice(0, Comment("            "), "~C"))),
    ")"
))


# BNGL to Python species

add('Map2k(s,R1~Y,R2~Y)',
Diagram(
   'MAP2K(',
    Choice(0, Comment("                                "), 's'),
    Choice(0, Comment("                                "), 
           Sequence('R1',
                    Choice(0, Comment("                "), '~Y')
           )),
    Choice(0, Comment("                                "), 
           Sequence('R2',
                    Choice(0, Comment("                "), '~Y')
           )),
    ')',
))
add('M1R(L,S228~u,S273~u,Arr,GRK,PP1,CK2)',
Diagram(
   'M1R(',
    Choice(0, Comment("                                "), 'L'),
    Choice(0, Comment("                                "), 
           Sequence('S228',
                    Choice(0, Comment("                "), '~u')
           )),
    Choice(0, Comment("                                "), 
           Sequence('S273',
                    Choice(0, Comment("                "), '~u')
           )),
    Choice(0, Comment("                                "), 'Arr'),
    Choice(0, Comment("                                "), 'GRK'),
    Choice(0, Comment("                                "), 'PP1'),
    Choice(0, Comment("                                "), 'CK2'),
    ')',
))
add('Oxo(R!1).M1R(L!1,S228~u,S273~u,Arr,GRK,PP1,CK2)',
Diagram(
   'Oxo(',
    Choice(0, Comment("                                "), 
           Sequence('R',
                    Choice(0, Comment("                "), '!1')
           )),
    ')',
    '.',
   'M1R(',
    Choice(0, Comment("                                "), 
           Sequence('L',
                    Choice(0, Comment("                "), '!1')
           )),
    Choice(0, Comment("                                "), 
           Sequence('S228',
                    Choice(0, Comment("                "), '~u')
           )),
    Choice(0, Comment("                                "), 
           Sequence('S273',
                    Choice(0, Comment("                "), '~u')
           )),
    Choice(0, Comment("                                "), 'Arr'),
    Choice(0, Comment("                                "), 'GRK'),
    Choice(0, Comment("                                "), 'PP1'),
    Choice(0, Comment("                                "), 'CK2'),
    ')',
))
add('Oxo(R!1).M1R(L!1,S228~p,S273~p,Arr!2,GRK,PP1,CK2).Arrestin(RLP!2,MEK!3,PP2A).MEK(Arr!3,ERK)',
Diagram(
   'Oxo(',
    Choice(0, Comment("                                "), 
           Sequence('R',
                    Choice(0, Comment("                "), '!1')
           )),
    ')',
    '.',
   'M1R(',
    Choice(0, Comment("                                "), 
           Sequence('L',
                    Choice(0, Comment("                "), '!1')
           )),
    Choice(0, Comment("                                "), 
           Sequence('S228',
                    Choice(0, Comment("                "), '~p')
           )),
    Choice(0, Comment("                                "), 
           Sequence('S273',
                    Choice(0, Comment("                "), '~p')
           )),
    Choice(0, Comment("                                "), 
           Sequence('Arr',
                    Choice(0, Comment("                "), '!2')
           )),
    Choice(0, Comment("                                "), 'GRK'),
    Choice(0, Comment("                                "), 'PP1'),
    Choice(0, Comment("                                "), 'CK2'),
    ')',
    '.',
   'Arrestin(',
    Choice(0, Comment("                                "), 
           Sequence('RLP',
                    Choice(0, Comment("                "), '!2')
           )),
    Choice(0, Comment("                                "), 
           Sequence('MEK',
                    Choice(0, Comment("                "), '!3')
           )),
    Choice(0, Comment("                                "), 'PP2A'),
    ')',
    '.',
   'MEK(',
    Choice(0, Comment("                                "), 
           Sequence('Arr',
                    Choice(0, Comment("                "), '!3')
           )),
    Choice(0, Comment("                                "), 'ERK'),
    ')',
))
add('Tie2(tie1bs,loc~sol,veptpbs,pY~dp,ang1bs,ang2bs)',
Diagram(
   'Tie2(',
    Choice(0, Comment("                                "), 'tie1bs'),
    Choice(0, Comment("                                "), 
           Sequence('loc',
                    Choice(0, Comment("                "), '~sol')
           )),
    Choice(0, Comment("                                "), 'veptpbs'),
    Choice(0, Comment("                                "), 
           Sequence('pY',
                    Choice(0, Comment("                "), '~dp')
           )),
    Choice(0, Comment("                                "), 'ang1bs'),
    Choice(0, Comment("                                "), 'ang2bs'),
    ')',
))
add('NFkB(Ikba!0,loc~cyt).IkBa(Nfkb!0,loc~cyt,Ser32_Ser36~0)',
Diagram(
   'NFkB(',
    Choice(0, Comment("                                "), 
           Sequence('Ikba',
                    Choice(0, Comment("                "), '!0')
           )),
    Choice(0, Comment("                                "), 
           Sequence('loc',
                    Choice(0, Comment("                "), '~cyt')
           )),
    ')',
    '.',
   'IkBa(',
    Choice(0, Comment("                                "), 
           Sequence('Nfkb',
                    Choice(0, Comment("                "), '!0')
           )),
    Choice(0, Comment("                                "), 
           Sequence('loc',
                    Choice(0, Comment("                "), '~cyt')
           )),
    Choice(0, Comment("                                "), 
           Sequence('Ser32_Ser36',
                    Choice(0, Comment("                "), '~0')
           )),
    ')',
))