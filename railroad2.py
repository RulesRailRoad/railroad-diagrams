# -*- coding: utf-8 -*-
from __future__ import annotations

import math as Math
import sys

bond_coords = {}
input_file = input('Python filepath: ')
print('\nOpening .html file for writing:', input_file+'.html')
sys.stdout = open(input_file+'.html', 'w')


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import (
        Any,
        Callable,
        Dict,
        Generator,
        List,
        Optional as Opt,
        Sequence as Seq,
        Tuple,
        Type,
        TypeVar,
        Union,
    )

    T = TypeVar("T")
    Node = Union[str, DiagramItem]  # pylint: disable=used-before-assignment
    WriterF = Callable[[str], Any]
    WalkerF = Callable[[DiagramItem], Any]  # pylint: disable=used-before-assignment
    AttrsT = Dict[str, Any]

# Display constants
DEBUG = False  # if true, writes some debug information into attributes
VS = 8  # minimum vertical separation between things. For a 3px stroke, must be at least 4
AR = 10  # radius of arcs
DIAGRAM_CLASS = "railroad-diagram"  # class to put on the root <svg>
STROKE_ODD_PIXEL_LENGTH = (
    True  # is the stroke width an odd (1px, 3px, etc) pixel length?
)
INTERNAL_ALIGNMENT = (
    "center"  # how to align items when they have extra space. left/right/center
)
CHAR_WIDTH = 8.5  # width of each monospace character. play until you find the right value for your font
COMMENT_CHAR_WIDTH = 7  # comments are in smaller text by default
ESCAPE_HTML = True  # Should Diagram.writeText() produce HTML-escaped text, or raw?


def escapeAttr(val: Union[str, float]) -> str:
    if isinstance(val, str):
        return val.replace("&", "&amp;").replace("'", "&apos;").replace('"', "&quot;")
    return f"{val:g}"


def escapeHtml(val: str) -> str:
    return escapeAttr(val).replace("<", "&lt;")


def determineGaps(outer: float, inner: float) -> Tuple[float, float]:
    diff = outer - inner
    if INTERNAL_ALIGNMENT == "left":
        return 0, diff
    elif INTERNAL_ALIGNMENT == "right":
        return diff, 0
    else:
        return diff / 2, diff / 2


def doubleenumerate(seq: Seq[T]) -> Generator[Tuple[int, int, T], None, None]:
    length = len(list(seq))
    for i, item in enumerate(seq):
        yield i, i - length, item


def addDebug(el: DiagramItem) -> None:
    if not DEBUG:
        return
    el.attrs["data-x"] = "{0} w:{1} h:{2}/{3}/{4}".format(
        type(el).__name__, el.width, el.up, el.height, el.down
    )


class DiagramItem:
    def __init__(self, name: str, attrs: Opt[AttrsT] = None, text: Opt[Node] = None):
        self.name = name
        # up = distance it projects above the entry line
        self.up: float = 0
        # height = distance between the entry/exit lines
        self.height: float = 0
        # down = distance it projects below the exit line
        self.down: float = 0
        # width = distance between the entry/exit lines horizontally
        self.width: float = 0
        # Whether the item is okay with being snug against another item or not
        self.needsSpace = False

        # DiagramItems pull double duty as SVG elements.
        self.attrs: AttrsT = attrs or {}
        # Subclasses store their meaningful children as .item or .items;
        # .children instead stores their formatted SVG nodes.
        self.children: List[Union[Node, Path, Style]] = [text] if text else []

    def format(self, x: float, y: float, width: float) -> DiagramItem:
        raise NotImplementedError  # Virtual

    def textDiagram() -> TextDiagram:
        raise NotImplementedError("Virtual")

    def addTo(self, parent: DiagramItem) -> DiagramItem:
        parent.children.append(self)
        return self

    def writeSvg(self, write: WriterF) -> None:
        write("<{0}".format(self.name))
        for name, value in sorted(self.attrs.items()):
            write(' {0}="{1}"'.format(name, escapeAttr(value)))
        write(">")
        if self.name in ["g", "svg"]:
            write("\n")
        for child in self.children:
            if isinstance(child, (DiagramItem, Path, Style)):
                child.writeSvg(write)
            else:
                write(escapeHtml(child))
        write("</{0}>".format(self.name))

    def walk(self, cb: WalkerF) -> None:
        cb(self)

    def __repr__(self) -> str:
        return f"DiagramItem({self.name}, {self.attrs}, {self.children})"


class DiagramMultiContainer(DiagramItem):
    def __init__(
        self,
        name: str,
        items: Seq[Node],
        attrs: Opt[Dict[str, str]] = None,
        text: Opt[str] = None,
    ):
        DiagramItem.__init__(self, name, attrs, text)
        self.items: List[DiagramItem] = [wrapString(item) for item in items]

    def format(self, x: float, y: float, width: float) -> DiagramItem:
        raise NotImplementedError  # Virtual

    def walk(self, cb: WalkerF) -> None:
        cb(self)
        for item in self.items:
            item.walk(cb)

    def __repr__(self) -> str:
        return f"DiagramMultiContainer({self.name}, {self.items}. {self.attrs}, {self.children})"


class Path:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.attrs = {"d": f"M{x} {y}"}

    def m(self, x: float, y: float) -> Path:
        self.attrs["d"] += f"m{x} {y}"
        return self

    def l(self, x: float, y: float) -> Path:
        self.attrs["d"] += f"l{x} {y}"
        return self

    def h(self, val: float) -> Path:
        self.attrs["d"] += f"h{val}"
        return self

    def right(self, val: float) -> Path:
        return self.h(max(0, val))

    def left(self, val: float) -> Path:
        return self.h(-max(0, val))

    def v(self, val: float) -> Path:
        self.attrs["d"] += f"v{val}"
        return self

    def down(self, val: float) -> Path:
        return self.v(max(0, val))

    def up(self, val: float) -> Path:
        return self.v(-max(0, val))

    def arc_8(self, start: str, dir: str) -> Path:
        # 1/8 of a circle
        arc = AR
        s2 = 1 / Math.sqrt(2) * arc
        s2inv = arc - s2
        sweep = "1" if dir == "cw" else "0"
        path = f"a {arc} {arc} 0 0 {sweep} "
        sd = start + dir
        offset: List[float]
        if sd == "ncw":
            offset = [s2, s2inv]
        elif sd == "necw":
            offset = [s2inv, s2]
        elif sd == "ecw":
            offset = [-s2inv, s2]
        elif sd == "secw":
            offset = [-s2, s2inv]
        elif sd == "scw":
            offset = [-s2, -s2inv]
        elif sd == "swcw":
            offset = [-s2inv, -s2]
        elif sd == "wcw":
            offset = [s2inv, -s2]
        elif sd == "nwcw":
            offset = [s2, -s2inv]
        elif sd == "nccw":
            offset = [-s2, s2inv]
        elif sd == "nwccw":
            offset = [-s2inv, s2]
        elif sd == "wccw":
            offset = [s2inv, s2]
        elif sd == "swccw":
            offset = [s2, s2inv]
        elif sd == "sccw":
            offset = [s2, -s2inv]
        elif sd == "seccw":
            offset = [s2inv, -s2]
        elif sd == "eccw":
            offset = [-s2inv, -s2]
        elif sd == "neccw":
            offset = [-s2, -s2inv]

        path += " ".join(str(x) for x in offset)
        self.attrs["d"] += path
        return self

    def arc(self, sweep: str) -> Path:
        x = AR
        y = AR
        if sweep[0] == "e" or sweep[1] == "w":
            x *= -1
        if sweep[0] == "s" or sweep[1] == "n":
            y *= -1
        cw = 1 if sweep in ("ne", "es", "sw", "wn") else 0
        self.attrs["d"] += f"a{AR} {AR} 0 0 {cw} {x} {y}"
        return self

    def addTo(self, parent: DiagramItem) -> Path:
        parent.children.append(self)
        return self

    def writeSvg(self, write: WriterF) -> None:
        write("<path")
        for name, value in sorted(self.attrs.items()):
            write(f' {name}="{escapeAttr(value)}"')
        write(" />")

    def format(self) -> Path:
        self.attrs["d"] += "h.5"
        return self

    def textDiagram(self) -> TextDiagram:
        return TextDiagram(0, 0, [])

    def __repr__(self) -> str:
        return f"Path({repr(self.x)}, {repr(self.y)})"


def wrapString(value: Node) -> DiagramItem:
    return value if isinstance(value, DiagramItem) else Terminal(value)


DEFAULT_STYLE = """\
	svg.railroad-diagram {
		background-color:hsl(0, 100%, 100%);
	}
	svg.railroad-diagram path {
		stroke-width:3;
		stroke:black;
        fill:rgba(0, 0, 0, 0);
		
	}
	svg.railroad-diagram text {
		font:bold 14px monospace;
		text-anchor:middle;
	}
	svg.railroad-diagram text.label{
		text-anchor:start;
	}
	svg.railroad-diagram text.comment{
		font:italic 12px monospace;
	}
	svg.railroad-diagram rect{
		stroke-width:3;
		stroke:black;
		fill:hsl(120,100%,90%);
	}
	svg.railroad-diagram rect.group-box {
		stroke: gray;
		stroke-dasharray: 10 5;
		fill: none;
	}

    .red {
    fill: red;
    }

    .green {
    fill: green;
    }

    .yellow {
    fill: yellow;
    }

    .blue {
    fill: blue;
    }

    .lightblue {
    fill: lightblue;
    }

    .skyblue {
    fill: skyblue;
    }

    .lightgreen {
    fill: lightgreen;
    }

    .orange {
    fill: orange;
    }

    .pink {
    fill: pink;
    }

    .violet {
    fill: violet;
    }

    .coral {
    fill: coral;
    }

    .lightsalmon {
    fill: lightsalmon;
    }

    .plum {
    fill: plum;
    }

    .turquoise {
    fill: turquoise;
    }
    

    .railroad-diagram .up-triangle polygon {
        stroke-width:3;
		stroke:black;
		fill:white
}
    .railroad-diagram .down-triangle polygon {
        stroke-width:3;
		stroke:black;
		fill:white
}

    .railroad-diagram .diamond polygon {
        stroke-width:3;
		stroke:black;
		fill:white
}

    svg.railroad-diagram path.right-bind {
    stroke: black;
    stroke-width: 3;
    fill: rgba(0, 0, 0, 0);
}
    svg.railroad-diagram g.terminal path.right-bind {
    stroke: black; 
    stroke-width: 3;
    fill: rgba(0, 0, 0, 0);
}
    svg.railroad-diagram g.nonterminal path.right-bind {
    stroke: black;
    stroke-width: 3;
    fill: rgba(0, 0, 0, 0);
}
"""


class Style:
    def __init__(self, css: str):
        self.css = css

    def __repr__(self) -> str:
        return f"Style({repr(self.css)})"

    def addTo(self, parent: DiagramItem) -> Style:
        parent.children.append(self)
        return self

    def format(self) -> Style:
        return self

    def textDiagram(self) -> TextDiagram:
        return TextDiagram(0, 0, [])

    def writeSvg(self, write: WriterF) -> None:
        # Write included stylesheet as CDATA. See https:#developer.mozilla.org/en-US/docs/Web/SVG/Element/style
        cdata = "/* <![CDATA[ */\n{css}\n/* ]]> */\n".format(css=self.css)
        write("<style>{cdata}</style>".format(cdata=cdata))


class Diagram(DiagramMultiContainer):
    def __init__(self, *items: Node, **kwargs: str):
        # Accepts a type=[simple|complex] kwarg
        DiagramMultiContainer.__init__(
            self,
            "svg",
            list(items),
            {
                "class": DIAGRAM_CLASS,
            },
        )
        self.type = kwargs.get("type", "simple")
        if items and not isinstance(items[0], Start):
            self.items.insert(0, Start(self.type))
        if items and not isinstance(items[-1], End):
            self.items.append(End(self.type))
        self.up = 0
        self.down = 0
        self.height = 0
        self.width = 0
        for item in self.items:
            if isinstance(item, Style):
                continue
            self.width += item.width + (20 if item.needsSpace else 0)
            self.up = max(self.up, item.up - self.height)
            self.height += item.height
            self.down = max(self.down - item.height, item.down)
        if self.items[0].needsSpace:
            self.width -= 10
        if self.items[-1].needsSpace:
            self.width -= 10
        self.formatted = False

    def __repr__(self) -> str:
        items = ", ".join(map(repr, self.items[1:-1]))
        pieces = [] if not items else [items]
        if self.type != "simple":
            pieces.append(f"type={repr(self.type)}")
        return f'Diagram({", ".join(pieces)})'

    def format(
        self,
        paddingTop: float = 20,
        paddingRight: Opt[float] = None,
        paddingBottom: Opt[float] = None,
        paddingLeft: Opt[float] = None,
    ) -> Diagram:
        if paddingRight is None:
            paddingRight = paddingTop
        if paddingBottom is None:
            paddingBottom = paddingTop
        if paddingLeft is None:
            paddingLeft = paddingRight
        assert paddingRight is not None
        assert paddingBottom is not None
        assert paddingLeft is not None
        x = paddingLeft
        y = paddingTop + self.up
        g = DiagramItem("g")
        if STROKE_ODD_PIXEL_LENGTH:
            g.attrs["transform"] = "translate(.5 .5)"
        for item in self.items:
            if item.needsSpace:
                Path(x, y).h(10).addTo(g)
                x += 10
            item.format(x, y, item.width).addTo(g)
            x += item.width
            y += item.height
            if item.needsSpace:
                Path(x, y).h(10).addTo(g)
                x += 10
        self.attrs["width"] = str(self.width + paddingLeft + paddingRight)
        self.attrs["height"] = str(
            self.up + self.height + self.down + paddingTop + paddingBottom * 8
        )
        self.attrs["viewBox"] = f"0 0 {self.attrs['width']} {self.attrs['height']}"
        global bond_coords
        for i,coords in enumerate(bond_coords.values()):
            if len(coords) >= 2:
                (x1, y1), (x2, y2) = coords[:2]

                offset = min(max(abs(y2-y1), i*10),i*8)
                vert = float(self.attrs["height"])/6 + offset+ i*25
                bottom_y = y1 + vert
                dist_up = bottom_y - y2
                
                path = Path(x1,y1).down(vert).right(x2-x1).up(dist_up)
                path.attrs["style"] = "stroke: black"
                path.addTo(g)
        bond_coords.clear()
        g.addTo(self)
        self.formatted = True
        return self
        

    def textDiagram(self) -> TextDiagram:
        (separator, ) = TextDiagram._getParts(["separator"])
        diagramTD = self.items[0].textDiagram()
        for item in self.items[1:]:
            itemTD = item.textDiagram()
            if item.needsSpace:
                itemTD = itemTD.expand(1, 1, 0, 0)
            diagramTD = diagramTD.appendRight(itemTD, separator)
        return diagramTD

    def writeSvg(self, write: WriterF) -> None:
        if not self.formatted:
            self.format()
        return DiagramItem.writeSvg(self, write)

    def writeText(self, write: WriterF) -> None:
        output = self.textDiagram()
        output = "\n".join(output.lines) + "\n"
        if ESCAPE_HTML:
            output = output.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
        write(output)

    def writeStandalone(self, write: WriterF, css: str | None = None) -> None:
        if not self.formatted:
            self.format()
        if css is None:
            css = DEFAULT_STYLE
        Style(css).addTo(self)
        self.attrs["xmlns"] = "http://www.w3.org/2000/svg"
        self.attrs['xmlns:xlink'] = "http://www.w3.org/1999/xlink"
        DiagramItem.writeSvg(self, write)
        self.children.pop()
        del self.attrs["xmlns"]
        del self.attrs["xmlns:xlink"]


class Sequence(DiagramMultiContainer):
    def __init__(self, *items: Node):
        DiagramMultiContainer.__init__(self, "g", items)
        self.needsSpace = True
        self.up = 0
        self.down = 0
        self.height = 0
        self.width = 0
        for item in self.items:
            self.width += item.width + (20 if item.needsSpace else 0)
            self.up = max(self.up, item.up - self.height)
            self.height += item.height
            self.down = max(self.down - item.height, item.down)
        if self.items[0].needsSpace:
            self.width -= 10
        if self.items[-1].needsSpace:
            self.width -= 10
        addDebug(self)

    def __repr__(self) -> str:
        items = ", ".join(repr(item) for item in self.items)
        return f"Sequence({items})"

    def format(self, x: float, y: float, width: float) -> Sequence:
        leftGap, rightGap = determineGaps(width, self.width)
        Path(x, y).h(leftGap).addTo(self)
        Path(x + leftGap + self.width, y + self.height).h(rightGap).addTo(self)
        x += leftGap
        for i, item in enumerate(self.items):
            if item.needsSpace and i > 0:
                Path(x, y).h(10).addTo(self)
                x += 10
            item.format(x, y, item.width).addTo(self)
            x += item.width
            y += item.height
            if item.needsSpace and i < len(self.items) - 1:
                Path(x, y).h(10).addTo(self)
                x += 10
        return self

    def textDiagram(self) -> TextDiagram:
        (separator, ) = TextDiagram._getParts(["separator"])
        diagramTD = TextDiagram(0, 0, [""])
        for item in self.items:
            itemTD = item.textDiagram()
            if item.needsSpace:
                itemTD = itemTD.expand(1, 1, 0, 0)
            diagramTD = diagramTD.appendRight(itemTD, separator)
        return diagramTD


class Choice(DiagramMultiContainer):
    def __init__(self, default: int, *items: Node, right_bind: bool = False, right_bind_color: str = 'black', bond_num: int = None):
        DiagramMultiContainer.__init__(self, "g", items)
        assert default < len(items)
        self.default = default
        self.width = AR * 4 + max(item.width for item in self.items)
        self.right_bind = right_bind
        self.right_bind_color = right_bind_color
        self.bond_num = bond_num

        # The size of the vertical separation between an item
        # and the following item.
        # The calcs are non-trivial and need to be done both here
        # and in .format(), so no reason to do it twice.
        self.separators: list[int] = [VS] * (len(items) - 1)

        # If the entry or exit lines would be too close together
        # to accommodate the arcs,
        # bump up the vertical separation to compensate.
        self.up = 0
        for i in range(default - 1, -1, -1):
            if i == default-1:
                arcs = AR * 2
            else:
                arcs = AR

            item = self.items[i]
            lowerItem = self.items[i+1]

            entryDelta = lowerItem.up + VS + item.down + item.height
            exitDelta = lowerItem.height + lowerItem.up + VS + item.down

            separator = VS
            if exitDelta < arcs or entryDelta < arcs:
                separator += max(arcs - entryDelta, arcs - exitDelta)
            self.separators[i] = separator
            self.up += lowerItem.up + separator + item.down + item.height
        self.up += self.items[0].up

        self.height = self.items[default].height

        for i in range(default+1, len(self.items)):
            if i == default+1:
                arcs = AR * 2
            else:
                arcs = AR

            item = self.items[i]
            upperItem = self.items[i-1]

            entryDelta = upperItem.height + upperItem.down + VS + item.up
            exitDelta = upperItem.down + VS + item.up + item.height

            separator = VS
            if entryDelta < arcs or exitDelta < arcs:
                separator += max(arcs - entryDelta, arcs - exitDelta)
            self.separators[i-1] = separator
            self.down += upperItem.down + separator + item.up + item.height
        self.down += self.items[-1].down
        addDebug(self)

    def __repr__(self) -> str:
        items = ", ".join(repr(item) for item in self.items)
        return f"Choice({self.default}, {items})"

    def format(self, x: float, y: float, width: float) -> Choice:
        leftGap, rightGap = determineGaps(width, self.width)

        # Hook up the two sides if self is narrower than its stated width.
        Path(x, y).h(leftGap).addTo(self)
        Path(x + leftGap + self.width, y + self.height).h(rightGap).addTo(self)
        x += leftGap

        if self.right_bind:
            path = Path(x + self.width, y).arc("ne").down(25)
            path.attrs["class"] = "bind"
            path.attrs["style"] = f'stroke: {self.right_bind_color};'
            path.addTo(self)

            if self.bond_num:
                cx = x + self.width + AR
                cy = y + AR + 25
                term = Terminal(self.bond_num, box_color="white")
                term.width *= 0.78
                term.format(cx - term.width / 2, cy, term.width).addTo(self)

        innerWidth = self.width - AR * 4
        default = self.items[self.default]

        # Do the elements that curve above
        distanceFromY = 0
        for i in range(self.default - 1, -1, -1):
            item = self.items[i]
            lowerItem = self.items[i+1]
            distanceFromY += lowerItem.up + self.separators[i] + item.down + item.height
            Path(x, y).arc("se").up(distanceFromY - AR * 2).arc("wn").addTo(self)
            item.format(x + AR * 2, y - distanceFromY, innerWidth).addTo(self)
            Path(x + AR * 2 + innerWidth, y - distanceFromY + item.height).arc(
                "ne"
            ).down(distanceFromY - item.height + default.height - AR * 2).arc(
                "ws"
            ).addTo(
                self
            )
        # Do the straight-line path.
        #Path(x, y).right(AR * 2).addTo(self)
        #self.items[self.default].format(x + AR * 2, y, innerWidth).addTo(self)
        #Path(x + AR * 2 + innerWidth, y + self.height).right(AR * 2).addTo(self)

        # Do the elements that curve below
        distanceFromY = 0
        for i in range(self.default+1, len(self.items)):
            item = self.items[i]
            upperItem = self.items[i-1]
            distanceFromY += upperItem.height + upperItem.down + self.separators[i-1] + item.up
            Path(x, y).arc("ne").down(distanceFromY - AR * 2).arc("ws").addTo(self)
            item.format(x + AR * 2, y + distanceFromY, innerWidth).addTo(self)
            Path(x + AR * 2 + innerWidth, y + distanceFromY + item.height).arc("se").up(
                distanceFromY - AR * 2 + item.height - default.height
            ).arc("wn").addTo(self)

        return self
            

    def textDiagram(self) -> TextDiagram:
        cross, line, line_vertical, roundcorner_bot_left, roundcorner_bot_right, roundcorner_top_left, roundcorner_top_right = TextDiagram._getParts(["cross", "line", "line_vertical", "roundcorner_bot_left", "roundcorner_bot_right", "roundcorner_top_left", "roundcorner_top_right"])
        # Format all the child items, so we can know the maximum width.
        itemTDs = []
        for item in self.items:
            itemTDs.append(item.textDiagram().expand(1, 1, 0, 0))
        max_item_width = max([i.width for i in itemTDs])
        diagramTD = TextDiagram(0, 0, [])
        # Format the choice collection.
        for itemNum, itemTD in enumerate(itemTDs):
            leftPad, rightPad = TextDiagram._gaps(max_item_width, itemTD.width)
            itemTD = itemTD.expand(leftPad, rightPad, 0, 0)
            hasSeparator = True
            leftLines = [line_vertical] * itemTD.height
            rightLines = [line_vertical] * itemTD.height
            moveEntry = False
            moveExit = False
            if itemNum <= self.default:
                # Item above the line: round off the entry/exit lines upwards.
                leftLines[itemTD.entry] = roundcorner_top_left
                rightLines[itemTD.exit] = roundcorner_top_right 
                if itemNum == 0:
                    # First item and above the line: also remove ascenders above the item's entry and exit, suppress the separator above it.
                    hasSeparator = False
                    for i in range(0, itemTD.entry):
                        leftLines[i] = " "
                    for i in range(0, itemTD.exit):
                        rightLines[i] = " "
            if itemNum >= self.default:
                # Item below the line: round off the entry/exit lines downwards.
                leftLines[itemTD.entry] = roundcorner_bot_left
                rightLines[itemTD.exit] = roundcorner_bot_right
                if itemNum == 0:
                    # First item and below the line: also suppress the separator above it.
                    hasSeparator = False
                if itemNum == (len(self.items) - 1):
                    # Last item and below the line: also remove descenders below the item's entry and exit
                    for i in range(itemTD.entry + 1, itemTD.height):
                        leftLines[i] = " "
                    for i in range(itemTD.exit + 1, itemTD.height):
                        rightLines[i] = " "
            if itemNum == self.default:
                # Item on the line: entry/exit are horizontal, and sets the outer entry/exit.
                leftLines[itemTD.entry] = cross
                rightLines[itemTD.exit] = cross
                moveEntry = True
                moveExit = True
                if itemNum == 0 and itemNum == (len(self.items) - 1):
                    # Only item and on the line: set entry/exit for straight through.
                    leftLines[itemTD.entry] = line
                    rightLines[itemTD.exit] = line
                elif itemNum == 0:
                    # First item and on the line: set entry/exit for no ascenders.
                    leftLines[itemTD.entry] = roundcorner_top_right
                    rightLines[itemTD.exit] = roundcorner_top_left
                elif itemNum == (len(self.items) - 1):
                    # Last item and on the line: set entry/exit for no descenders.
                    leftLines[itemTD.entry] = roundcorner_bot_right
                    rightLines[itemTD.exit] = roundcorner_bot_left
            leftJointTD = TextDiagram(itemTD.entry, itemTD.entry, leftLines)
            rightJointTD = TextDiagram(itemTD.exit, itemTD.exit, rightLines)
            itemTD = leftJointTD.appendRight(itemTD, "").appendRight(rightJointTD, "")
            separator = [line_vertical + (" " * (TextDiagram._maxWidth(diagramTD, itemTD) - 2)) + line_vertical] if hasSeparator else []
            diagramTD = diagramTD.appendBelow(itemTD, separator, moveEntry=moveEntry, moveExit=moveExit)
        return diagramTD

class MultipleChoice(DiagramMultiContainer):
    def __init__(self, default: int, type: str, *items: Node):
        DiagramMultiContainer.__init__(self, "g", items)
        assert 0 <= default < len(items)
        assert type in ["up-arrow", "down-arrow"]
        self.default = default
        self.type = type
        self.needsSpace = True
        self.innerWidth = max(item.width for item in self.items)
        self.width = 30 + AR + self.innerWidth + AR + 20
        self.up = self.items[0].up
        self.down = self.items[-1].down
        self.height = self.items[default].height
        for i, item in enumerate(self.items):
            if i in [default - 1, default + 1]:
                minimum = 10 + AR
            else:
                minimum = AR
            if i < default:
                self.up += max(
                    minimum, item.height + item.down + VS + self.items[i + 1].up
                )
            elif i == default:
                continue
            else:
                self.down += max(
                    minimum,
                    item.up + VS + self.items[i - 1].down + self.items[i - 1].height,
                )
        self.down -= self.items[default].height  # already counted in self.height
        addDebug(self)

    def __repr__(self) -> str:
        items = ", ".join(repr(item) for item in self.items)
        return f"MultipleChoice({repr(self.default)}, {repr(self.type)}, {items})"

    def format(self, x: float, y: float, width: float) -> MultipleChoice:
        leftGap, rightGap = determineGaps(width, self.width)

        # Hook up the two sides if self is narrower than its stated width.
        Path(x, y).h(leftGap+10).addTo(self)
        Path(x + leftGap + self.width, y + self.height).h(rightGap).addTo(self)
        x += leftGap

        default = self.items[self.default]

        # Do the elements that curve above
        above = self.items[: self.default][::-1]
        if above:
            distanceFromY = max(
                10 + AR, default.up + VS + above[0].down + above[0].height
            )
        for i, ni, item in doubleenumerate(above):
            (Path(x + 30, y).up(distanceFromY - AR).arc("wn").addTo(self))
            item.format(x + 30 + AR, y - distanceFromY, self.innerWidth).addTo(self)
            (
                Path(x + 30 + AR + self.innerWidth, y - distanceFromY + item.height)
                .arc("ne")
                .down(distanceFromY - item.height + default.height - AR - 10)
                .addTo(self)
            )
            if ni < -1:
                distanceFromY += max(
                    AR, item.up + VS + above[i + 1].down + above[i + 1].height
                )

        # Do the straight-line path.
        Path(x + 30, y).right(AR).addTo(self)
        self.items[self.default].format(x + 30 + AR, y, self.innerWidth).addTo(self)
        Path(x + 30 + AR + self.innerWidth, y + self.height).right(AR).addTo(self)

        # Do the elements that curve below
        below = self.items[self.default + 1 :]
        if below:
            distanceFromY = max(
                10 + AR, default.height + default.down + VS + below[0].up
            )
        for i, item in enumerate(below):
            (Path(x + 30, y).down(distanceFromY - AR).arc("ws").addTo(self))
            item.format(x + 30 + AR, y + distanceFromY, self.innerWidth).addTo(self)
            (
                Path(x + 30 + AR + self.innerWidth, y + distanceFromY + item.height)
                .arc("se")
                .up(distanceFromY - AR + item.height - default.height - 10)
                .addTo(self)
            )
            distanceFromY += max(
                AR,
                item.height
                + item.down
                + VS
                + (below[i + 1].up if i + 1 < len(below) else 0),
            )
        text = DiagramItem("g", attrs={"class": "diagram-text"}).addTo(self)
        DiagramItem(
            "title",
            text="take one or more branches, once each, in any order"
            if self.type == "up-arrow"
            else "take all branches, once each, in any order",
        ).addTo(text)
        DiagramItem(
            "path",
            attrs={
                "d": "M {x} {y} h -16 a 4 4 0 0 0 -4 4 v 12 a 4 4 0 0 0 4 4 h 16 z".format(
                    x=x + 30, y=y - 10
                ),
                "class": "diagram-text",
                "style": "fill: orange",
            },
        ).addTo(text)
        DiagramItem(
            "text",
            text="⬆" if self.type == "up-arrow" else "⬇",
            attrs={"x": x + 20, "y": y + 6, "class": "diagram-text"},
        ).addTo(text)
        DiagramItem(
            "path",
            attrs={
                "d": "M {x} {y} h 16 a 4 4 0 0 1 4 4 v 12 a 4 4 0 0 1 -4 4 h -16 z".format(
                    x=x + self.width - 20, y=y - 10
                ),
                "class": "diagram-text",
                "style": "fill: orange",
            },
        ).addTo(text)
        DiagramItem(
            "text",
            text="⬆" if self.type == "up-arrow" else "⬇",
            attrs={"x": x + self.width - 10, "y": y + 6, "class": "diagram-text"},
        ).addTo(text)
        return self

    def textDiagram(self) -> TextDiagram:
        (multi_repeat,) = TextDiagram._getParts(["multi_repeat"])
        anyAll = TextDiagram.rect("⬆" if self.type == "up-arrow" else "⬇")
        diagramTD = Choice.textDiagram(self)
        repeatTD = TextDiagram.rect(multi_repeat)
        diagramTD = anyAll.appendRight(diagramTD, "")
        diagramTD = diagramTD.appendRight(repeatTD, "")
        return diagramTD



class Start(DiagramItem):
    def __init__(self, type: str = "simple", label: Opt[str] = None):
        DiagramItem.__init__(self, "g")
        if label:
            self.width = max(20, len(label) * CHAR_WIDTH + 10)
        else:
            self.width = 20
        self.up = 10
        self.down = 10
        self.type = type
        self.label = label
        addDebug(self)

    def format(self, x: float, y: float, width: float) -> Start:
        path = Path(x, y - 10)
        if self.type == "complex":
            path.down(20).m(0, -10).right(self.width).addTo(self)
        else:
            path.down(20).m(10, -20).down(20).m(-10, -10).right(self.width).addTo(self)
        if self.label:
            DiagramItem(
                "text",
                attrs={"x": x, "y": y - 15, "style": "text-anchor:start"},
                text=self.label,
            ).addTo(self)
        return self

    def textDiagram(self) -> TextDiagram:
        cross, line, tee_right = TextDiagram._getParts(["cross", "line", "tee_right"])
        if self.type == "simple":
            start = tee_right + cross + line
        else:
            start = tee_right + line
        labelTD = TextDiagram(0, 0, [])
        if self.label:
            labelTD = TextDiagram(0, 0, [self.label])
            start = TextDiagram._padR(start, labelTD.width, line)
        startTD = TextDiagram(0, 0, [start])
        return labelTD.appendBelow(startTD, [], moveEntry=True, moveExit=True)

    def __repr__(self) -> str:
        return f"Start(type={repr(self.type)}, label={repr(self.label)})"


class End(DiagramItem):
    def __init__(self, type: str = "simple"):
        DiagramItem.__init__(self, "path")
        self.width = 20
        self.up = 10
        self.down = 10
        self.type = type
        addDebug(self)

    def format(self, x: float, y: float, width: float) -> End:
        if self.type == "simple":
            self.attrs["d"] = "M {0} {1} h 20 m -10 -10 v 20 m 10 -20 v 20".format(x, y)
        elif self.type == "complex":
            self.attrs["d"] = "M {0} {1} h 20 m 0 -10 v 20".format(x, y)
        return self

    def textDiagram(self) -> TextDiagram:
        cross, line, tee_left = TextDiagram._getParts(["cross", "line", "tee_left"])
        if self.type == "simple":
            end = line + cross + tee_left
        else:
            end = line + tee_left
        return TextDiagram(0, 0, [end])

    def __repr__(self) -> str:
        return f"End(type={repr(self.type)})"
    

class EndWhiteSpace(DiagramItem):
    def __init__(self, type: str = "simple"):
            DiagramItem.__init__(self, "path")
            self.width = 10
            self.up = 10
            self.down = 10
            self.type = type
            addDebug(self)

    def format(self, x: float, y: float, width: float) -> End:
            if self.type == "simple":
                self.attrs["d"] = (
                    f"M {x} {y - 10} v 20 "            
                    f"M {x + 10} {y - 10} v 20"         
                )
            elif self.type == "complex":
                self.attrs["d"] = (
                    f"M {x + 20} {y - 10} v 20"         
                )
            return self

    def textDiagram(self) -> TextDiagram:
        bar = "│"
        space = "  "
        if self.type == "simple":
            end = bar + space + bar
        else:
            end = bar
        return TextDiagram(0, 0, [end])

    def __repr__(self) -> str:
            return f"End(type={repr(self.type)})"

class Terminal(DiagramItem):
    def __init__(
        self, text: str, href: Opt[str] = None, title: Opt[str] = None, cls: str = "", box_color: Opt[str]=None, 
        right_bind: bool = False, bottom_bind: bool = False, top_bind: bool = False, right_bind_color: Opt[str] = 'black',
        bottom_bind_color: Opt[str] = 'black', top_bind_color: Opt[str] = 'black', bond_num: int = None, bond_type: str = 'circle'
        , wrap: bool = False
    ):
        DiagramItem.__init__(self, "g", {"class": " ".join(["terminal", cls])})
        self.text = text
        self.href = href
        self.title = title
        self.cls = cls
        self.box_color = box_color

        self.right_bind = right_bind
        self.right_bind_color = right_bind_color

        self.bottom_bind = bottom_bind
        self.bottom_bind_color = bottom_bind_color

        self.top_bind = top_bind
        self.top_bind_color = top_bind_color

        self.bond_num = bond_num
        self.bond_type = bond_type
        self.wrap = wrap
        
        self.width = len(text) * CHAR_WIDTH + 20
        self.up = 11
        self.down = 11
        self.needsSpace = True
        addDebug(self)

    def __repr__(self) -> str:
        return f"Terminal({repr(self.text)}, href={repr(self.href)}, title={repr(self.title)}, cls={repr(self.cls)})"

    def format(self, x: float, y: float, width: float) -> Terminal:
        self.formatted_x = x
        self.formatted_y = y
        self.formatted_width = width
        leftGap, rightGap = determineGaps(width, self.width)

        # Hook up the two sides if self is narrower than its stated width.
        Path(x, y).h(leftGap).addTo(self)
        Path(x + leftGap + self.width, y).h(rightGap).addTo(self)

        
        if self.right_bind:
            path = Path(x + self.width, y).arc("ne").down(25)
            path.attrs["class"] = "right-bind"
            path.attrs["style"] = f"stroke: {self.right_bind_color}"
            path.addTo(self)

            if self.bond_num:
                cx = x + self.width + AR
                cy = y + AR + 25
                term = Terminal(self.bond_num, box_color="white")
                term.width *= 0.78
                term.format(cx - term.width / 2, cy, term.width).addTo(self)

        if self.bottom_bind:
            if self.wrap:
                arc_start = x - AR
                arc_height = AR*1.5

                path = Path(arc_start, y-AR/2)
                path.down(arc_height).arc('ws').right((self.width)/4).arc('ne').arc('wn').right((self.width)/4).arc("se").up(arc_height)
                path.attrs["class"] = "bottom-bind"
                path.attrs["style"] = f"stroke: gray; stroke-dasharray: 4,2"
                path.addTo(self)
            else:
                horiz_dist = width / 2 - AR
                path1 = Path(x, y + self.height).arc("nw").arc("ws").right(horiz_dist).arc("ne").down(self.height)

                style = f"stroke: {self.bottom_bind_color}"
                if self.bottom_bind_color.strip() == "gray":
                    style += "; stroke-dasharray: 4,2"

                path1.attrs["class"] = "bottom-bind"
                path1.attrs["style"] = style
                path1.addTo(self)

                path2 = Path(x + width, y + self.height).arc("ne").arc("es").left(horiz_dist).arc("nw").down(self.height)
                path2.attrs["class"] = "bottom-bind"
                path2.attrs["style"] = style
                path2.addTo(self)

                if self.bond_num and self.bond_num != "?" and self.bond_num != "+":
                    cx = 0
                    cy = 0
                    if self.bond_type == 'circle':
                        cx = x + self.width / 2
                        cy = y + self.height + AR * 4
                        term = Terminal(self.bond_num, box_color="white")
                        term.width *= 0.78
                        term.format(cx - term.width / 2, cy, term.width).addTo(self)
                    if self.bond_type == 'nrbroken':
                        cx = x + self.width / 2
                        cy = y + self.height + AR * 5
                        up = NonTerminal("⬆", box_color="orange")
                        up_height = up.up + up.down -2
                        up.width *= 0.75
                        up.format(cx - up.width / 2, cy-up_height+up.up, up.width).addTo(self)

                        down = NonTerminal(self.bond_num, box_color="white")
                        down.width *= 0.75
                        down.format(cx-down.width/2, cy+up_height/2, down.width).addTo(self)
                    if self.bond_type == 'nradded':
                        cx = x + self.width / 2
                        cy = y + self.height + AR * 5
                        up = NonTerminal("⬇", box_color="orange")
                        up_height = up.up + up.down -2
                        up.width *= 0.75
                        up.format(cx - up.width / 2, cy-up_height+up.up, up.width).addTo(self)

                        down = NonTerminal(self.bond_num, box_color="white")
                        down.width *= 0.75
                        down.format(cx-down.width/2, cy+up_height/2, down.width).addTo(self)
                    if self.bond_type == 'radded':
                        cx = x + self.width / 2
                        cy = y + self.height + AR * 5
                        up = NonTerminal("⬆⬇", box_color="orange")
                        up_height = up.up + up.down -2
                        up.width *= 0.75
                        up.format(cx - up.width / 2, cy-up_height+up.up, up.width).addTo(self)

                        down = NonTerminal(self.bond_num, box_color="white")
                        down.format(cx-down.width/2, cy+up_height/2, down.width).addTo(self)
                    if self.bond_type == 'rbroken':
                        cx = x + self.width / 2
                        cy = y + self.height + AR * 5
                        up = NonTerminal("⬆⬇", box_color="orange")
                        up_height = up.up + up.down -2
                        up.width *= 0.75
                        up.format(cx - up.width / 2, cy-up_height+up.up, up.width).addTo(self)

                        down = NonTerminal(self.bond_num, box_color="white")
                        down.format(cx-down.width/2, cy+up_height/2, down.width).addTo(self)
                    global bond_coords
                    if self.bond_type == 'circle':
                        cy += term.height / 2 + term.down  # Term is your circle box
                    elif 'down' in locals() and hasattr(down, 'formatted_y'):
                        cy = down.formatted_y + down.height / 2 + down.down
                    bond_coords.setdefault(self.bond_num, []).append((cx, cy))

        if self.top_bind:
            horiz_dist = self.width / 2 - AR
            path1 = Path(x, y - self.height).arc("sw").arc("wn").right(horiz_dist).arc("se").up(self.height)
            path1.attrs["class"] = "top-bind"
            path1.attrs["style"] = f"stroke: {self.top_bind_color}; fill: none"
            path1.addTo(self)

            path2 = Path(x + self.width, y - self.height).arc("se").arc("en").left(horiz_dist).arc("sw").up(self.height)
            path2.attrs["class"] = "top-bind"
            path2.attrs["style"] = f"stroke: {self.top_bind_color}; fill: none"
            path2.addTo(self)
            
        rect_attrs = {
            "x": x + leftGap,
            "y": y - 11,
            "width": self.width,
            "height": self.up + self.down,
            "rx": AR,
            "ry": AR,
            }

        if self.box_color is not None:
            rect_attrs["style"] = f"fill: {self.box_color}"

        DiagramItem("rect", rect_attrs).addTo(self)
    
        text = DiagramItem(
                "text", {"x": x + leftGap + self.width / 2, "y": y + 4}, self.text
        )
        if self.href is not None:
            a = DiagramItem("a", {"xlink:href": self.href}, text).addTo(self)
            text.addTo(a)
        else:
            text.addTo(self)
        if self.title is not None:
            DiagramItem("title", {}, self.title).addTo(self)
        return self

    def textDiagram(self) -> TextDiagram:
        # Note: href, title, and cls are ignored for text diagrams.
        return TextDiagram.roundrect(self.text)


class NonTerminal(DiagramItem):
    def __init__(
        self, text: str, href: Opt[str] = None, title: Opt[str] = None, cls: str = "", box_color: Opt[str]=None, 
        right_bind: bool = False, bottom_bind: bool = False, top_bind: bool = False, right_bind_color: Opt[str] = 'black',
        bottom_bind_color: Opt[str] = 'black', top_bind_color: Opt[str] = 'black', bond_num: int = None, bond_type: str = 'circle'
        , wrap: bool = False
    ):
        DiagramItem.__init__(self, "g", {"class": " ".join(["non-terminal", cls])})
        self.text = text
        self.href = href
        self.title = title
        self.cls = cls
        self.box_color = box_color

        self.right_bind = right_bind
        self.right_bind_color = right_bind_color

        self.bottom_bind = bottom_bind
        self.bottom_bind_color = bottom_bind_color

        self.top_bind = top_bind
        self.top_bind_color = top_bind_color

        self.bond_num = bond_num
        self.bond_type = bond_type
        self.wrap = wrap

        self.width = len(text) * CHAR_WIDTH + 20
        self.up = 11
        self.down = 11
        self.needsSpace = True
        addDebug(self)

    def __repr__(self) -> str:
        return f"NonTerminal({repr(self.text)}, href={repr(self.href)}, title={repr(self.title)}, cls={repr(self.cls)})"

    def format(self, x: float, y: float, width: float) -> NonTerminal:
        self.formatted_x = x
        self.formatted_y = y
        self.formatted_width = width
        leftGap, rightGap = determineGaps(width, self.width)

        # Hook up the two sides if self is narrower than its stated width.
        Path(x, y).h(leftGap).addTo(self)
        Path(x + leftGap + self.width, y).h(rightGap).addTo(self)

        if self.right_bind:
            path = Path(x + self.width, y).arc("ne").down(25)
            path.attrs["class"] = "right-bind"
            path.attrs["style"] = f"stroke: {self.right_bind_color}"
            path.addTo(self)

            if self.bond_num:
                cx = x + self.width + AR
                cy = y + AR + 25
                term = Terminal(self.bond_num, box_color="white")
                term.width *= 0.78
                term.format(cx - term.width / 2, cy, term.width).addTo(self)

        if self.bottom_bind:
            if self.wrap:
                arc_start = x - AR
                arc_height = AR*1.5

                path1 = Path(arc_start, y-AR/2)
                path1.down(arc_height).arc('ws').right((width)/2-AR).arc('ne')
                path1.attrs["class"] = "bottom-bind"
                path1.attrs["style"] = f"stroke: gray; stroke-dasharray: 4,2"
                path1.addTo(self)

                path2 = Path(x + AR + width, y-AR/2)
                path2.down(arc_height).arc("es").left(width/2-AR).arc("nw")
                path2.attrs["class"] = "bottom-bind"
                path2.attrs["style"] = f"stroke: gray; stroke-dasharray: 4,2"
                path2.addTo(self)
            else:
                horiz_dist = width / 2 - AR
                path1 = Path(x, y + self.height).arc("nw").arc("ws").right(horiz_dist).arc("ne").down(self.height)

                style = f"stroke: {self.bottom_bind_color}"
                if self.bottom_bind_color.strip() == "gray":
                    style += "; stroke-dasharray: 4,2"

                path1.attrs["class"] = "bottom-bind"
                path1.attrs["style"] = style
                path1.addTo(self)

                path2 = Path(x + width, y + self.height).arc("ne").arc("es").left(horiz_dist).arc("nw").down(self.height)
                path2.attrs["class"] = "bottom-bind"
                path2.attrs["style"] = style
                path2.addTo(self)

                if self.bond_num and self.bond_num != "?" and self.bond_num != "+":
                    cx=0
                    cy=0
                    if self.bond_type == 'circle':
                        cx = x + width / 2
                        cy = y + self.height + AR * 4
                        term = Terminal(self.bond_num, box_color="white")
                        term.width *= 0.78
                        term.format(cx - term.width / 2, cy, term.width).addTo(self)
                    if self.bond_type == 'nrbroken':
                        cx = x + width / 2
                        cy = y + self.height + AR * 5
                        up = NonTerminal("⬆", box_color="orange")
                        up_height = up.up + up.down -2
                        up.width *= 0.75
                        up.format(cx - up.width / 2, cy-up_height+up.up, up.width).addTo(self)

                        down = NonTerminal(self.bond_num, box_color="white")
                        down.width *= 0.75
                        down.format(cx-down.width/2, cy+up_height/2, down.width).addTo(self)
                    if self.bond_type == 'nradded':
                        cx = x + width / 2
                        cy = y + self.height + AR * 5
                        up = NonTerminal("⬇", box_color="orange")
                        up_height = up.up + up.down -2
                        up.width *= 0.75
                        up.format(cx - up.width / 2, cy-up_height+up.up, up.width).addTo(self)

                        down = NonTerminal(self.bond_num, box_color="white")
                        down.width *= 0.75
                        down.format(cx-down.width/2, cy+up_height/2, down.width).addTo(self)
                    if self.bond_type == 'radded':
                        cx = x + width / 2
                        cy = y + self.height + AR * 5
                        up = NonTerminal("⬆⬇", box_color="orange")
                        up_height = up.up + up.down -2
                        up.width *= 0.75
                        up.format(cx - up.width / 2, cy-up_height+up.up, up.width).addTo(self)

                        down = NonTerminal(self.bond_num, box_color="white")
                        down.format(cx-down.width/2, cy+up_height/2, down.width).addTo(self)
                    if self.bond_type == 'rbroken':
                        cx = x + width / 2
                        cy = y + self.height + AR * 5
                        up = NonTerminal("⬆⬇", box_color="orange")
                        up_height = up.up + up.down -2
                        up.width *= 0.75
                        up.format(cx - up.width / 2, cy-up_height+up.up, up.width).addTo(self)

                        down = NonTerminal(self.bond_num, box_color="white")
                        down.format(cx-down.width/2, cy+up_height/2, down.width).addTo(self)
                    global bond_coords
                    if self.bond_type == 'circle':
                        cy += term.height / 2 + term.down  # Term is your circle box
                    elif 'down' in locals() and hasattr(down, 'formatted_y'):
                        cy = down.formatted_y + down.height / 2 + down.down
                    bond_coords.setdefault(self.bond_num, []).append((cx, cy))
        
        if self.top_bind:
            horiz_dist = self.width / 2 - AR
            path1 = Path(x, y - self.height).arc("sw").arc("wn").right(horiz_dist).arc("se").up(self.height)
            path1.attrs["class"] = "top-bind"
            path1.attrs["style"] = f"stroke: {self.top_bind_color}"
            path1.addTo(self)

            path2 = Path(x + self.width, y - self.height).arc("se").arc("en").left(horiz_dist).arc("sw").up(self.height)
            path2.attrs["class"] = "top-bind"
            path2.attrs["style"] = f"stroke: {self.top_bind_color}"
            path2.addTo(self)

        rect_attrs = {
            "x": x + leftGap,
            "y": y - 11,
            "width": self.width,
            "height": self.up + self.down,
            }
        if self.box_color is not None:
            rect_attrs["style"] = f"fill: {self.box_color}"

        DiagramItem("rect", rect_attrs).addTo(self)
        text = DiagramItem(
            "text", {"x": x + leftGap + self.width / 2, "y": y + 4}, self.text
        )
        if self.href is not None:
            a = DiagramItem("a", {"xlink:href": self.href}, text).addTo(self)
            text.addTo(a)
        else:
            text.addTo(self)
        if self.title is not None:
            DiagramItem("title", {}, self.title).addTo(self)
        return self

    def textDiagram(self) -> TextDiagram:
        # Note: href, title, and cls are ignored for text diagrams.
        return TextDiagram.rect(self.text)


class UpTriangle(DiagramItem):
    def __init__(
        self, text: str, href: Opt[str] = None, title: Opt[str] = None, cls: str = "", box_color: Opt[str]=None,
    ):
        DiagramItem.__init__(self, "g", {"class": " ".join(["up-triangle", cls])})
        self.text = text
        self.href = href
        self.title = title
        self.cls = cls
        self.box_color = box_color
        self.width = len(text) * CHAR_WIDTH + 30
        self.up = 15
        self.down = 15
        self.needsSpace = True
        addDebug(self)

    def __repr__(self) -> str:
        return f"UpTriangle({repr(self.text)}, href={repr(self.href)}, title={repr(self.title)}, cls={repr(self.cls)})"

    def format(self, x: float, y: float, width: float) -> DiagramItem:
        leftGap, rightGap = determineGaps(width, self.width)

        Path(x, y).h(leftGap).addTo(self)
        Path(x + leftGap + self.width, y).h(rightGap).addTo(self)

        top = y - self.up -5
        bottom = y + self.down -5
        points = [
            (x + leftGap + self.width/2, top),
            (x + leftGap, bottom),
            (x + leftGap+ self.width, bottom),
        ]
        point_str = " ".join(f"{px},{py}" for px, py in points)

        polygon_attrs = {
            "points": point_str,

        }

        if self.box_color:
            polygon_attrs["style"] = f"fill: {self.box_color}; stroke: black"

        DiagramItem("polygon", polygon_attrs).addTo(self)

        text = DiagramItem(
            "text", {"x": x + leftGap + self.width / 2, "y": y + 4}, self.text
        )

        if self.href is not None:
            a = DiagramItem("a", {"xlink:href": self.href}, text).addTo(self)
            text.addTo(a)
        else:
            text.addTo(self)
        if self.title is not None:
            DiagramItem("title", {}, self.title).addTo(self)

        return self

    def textDiagram(self) -> TextDiagram:
        return TextDiagram.other(self.text)


class DownTriangle(DiagramItem):
    def __init__(
        self, text: str, href: Opt[str] = None, title: Opt[str] = None, cls: str = "", box_color: Opt[str]=None,
    ):
        DiagramItem.__init__(self, "g", {"class": " ".join(["down-triangle", cls])})
        self.text = text
        self.href = href
        self.title = title
        self.cls = cls
        self.box_color = box_color
        self.width = len(text) * CHAR_WIDTH + 30
        self.up = 15
        self.down = 15
        self.needsSpace = True
        addDebug(self)

    def __repr__(self) -> str:
        return f"DownTriangle({repr(self.text)}, href={repr(self.href)}, title={repr(self.title)}, cls={repr(self.cls)})"

    def format(self, x: float, y: float, width: float) -> DiagramItem:
        leftGap, rightGap = determineGaps(width, self.width)

        Path(x, y).h(leftGap).addTo(self)
        Path(x + leftGap + self.width, y).h(rightGap).addTo(self)

        top = y - self.up -5
        bottom = y + self.down-5
        points = [
            (x + leftGap + self.width/2, bottom),
            (x + leftGap, top),
            (x + leftGap + self.width, top),
        ]
        point_str = " ".join(f"{px},{py}" for px, py in points)

        polygon_attrs = {
            "points": point_str,

        }

        if self.box_color:
            polygon_attrs["style"] = f"fill: {self.box_color}; stroke: black"

        DiagramItem("polygon", polygon_attrs).addTo(self)

        text = DiagramItem(
            "text", {"x": x + leftGap + self.width / 2, "y": y -2}, self.text
        )

        if self.href is not None:
            a = DiagramItem("a", {"xlink:href": self.href}, text).addTo(self)
            text.addTo(a)
        else:
            text.addTo(self)
        if self.title is not None:
            DiagramItem("title", {}, self.title).addTo(self)

        return self

    def textDiagram(self) -> TextDiagram:
        return TextDiagram.other(self.text)

class UpTriangle(DiagramItem):
    def __init__(
        self, text: str, href: Opt[str] = None, title: Opt[str] = None, cls: str = "", box_color: Opt[str]=None,
    ):
        DiagramItem.__init__(self, "g", {"class": " ".join(["up-triangle", cls])})
        self.text = text
        self.href = href
        self.title = title
        self.cls = cls
        self.box_color = box_color
        self.width = len(text) * CHAR_WIDTH + 30
        self.up = 15
        self.down = 15
        self.needsSpace = True
        addDebug(self)

    def __repr__(self) -> str:
        return f"UpTriangle({repr(self.text)}, href={repr(self.href)}, title={repr(self.title)}, cls={repr(self.cls)})"

    def format(self, x: float, y: float, width: float) -> DiagramItem:
        leftGap, rightGap = determineGaps(width, self.width)

        Path(x, y).h(leftGap).addTo(self)
        Path(x + leftGap + self.width, y).h(rightGap).addTo(self)

        top = y - self.up -5
        bottom = y + self.down -5
        points = [
            (x + leftGap + self.width/2, top),
            (x + leftGap, bottom),
            (x + leftGap+ self.width, bottom),
        ]
        point_str = " ".join(f"{px},{py}" for px, py in points)

        polygon_attrs = {
            "points": point_str,

        }

        if self.box_color:
            polygon_attrs["style"] = f"fill: {self.box_color}; stroke: black"

        DiagramItem("polygon", polygon_attrs).addTo(self)

        text = DiagramItem(
            "text", {"x": x + leftGap + self.width / 2, "y": y + 4}, self.text
        )

        if self.href is not None:
            a = DiagramItem("a", {"xlink:href": self.href}, text).addTo(self)
            text.addTo(a)
        else:
            text.addTo(self)
        if self.title is not None:
            DiagramItem("title", {}, self.title).addTo(self)

        return self

    def textDiagram(self) -> TextDiagram:
        return TextDiagram.other(self.text)


class Diamond(DiagramItem):
    def __init__(
        self, text: str, href: Opt[str] = None, title: Opt[str] = None, cls: str = "", box_color: Opt[str]=None,
    ):
        DiagramItem.__init__(self, "g", {"class": " ".join(["diamond", cls])})
        self.text = text
        self.href = href
        self.title = title
        self.cls = cls
        self.box_color = box_color
        self.width = len(text) * CHAR_WIDTH + 30
        self.up = 15
        self.down = 15
        self.needsSpace = True
        addDebug(self)

    def __repr__(self) -> str:
        return f"Diamond({repr(self.text)}, href={repr(self.href)}, title={repr(self.title)}, cls={repr(self.cls)})"

    def format(self, x: float, y: float, width: float) -> DiagramItem:
        leftGap, rightGap = determineGaps(width, self.width)

        Path(x, y).h(leftGap).addTo(self)
        Path(x + leftGap + self.width, y).h(rightGap).addTo(self)

        top = y - self.up -3
        bottom = y + self.down+3
        left = x + leftGap
        right = x + leftGap + self.width
        center = x + leftGap + self.width /2

        points = [
            (center, top),
            (right, y),
            (center, bottom),
            (left, y)
        ]
        point_str = " ".join(f"{px},{py}" for px, py in points)

        polygon_attrs = {
            "points": point_str,

        }

        if self.box_color:
            polygon_attrs["style"] = f"fill: {self.box_color}; stroke: black"

        DiagramItem("polygon", polygon_attrs).addTo(self)

        text = DiagramItem(
            "text", {"x": center, "y": y + 4}, self.text
        )

        if self.href is not None:
            a = DiagramItem("a", {"xlink:href": self.href}, text).addTo(self)
            text.addTo(a)
        else:
            text.addTo(self)
        if self.title is not None:
            DiagramItem("title", {}, self.title).addTo(self)

        return self

    def textDiagram(self) -> TextDiagram:
        return TextDiagram.other(self.text)

class Comment(DiagramItem):
    def __init__(
        self, text: str, href: Opt[str] = None, title: Opt[str] = None, cls: str = ""
    ):
        DiagramItem.__init__(self, "g", {"class": " ".join(["non-terminal", cls])})
        self.text = text
        self.href = href
        self.title = title
        self.cls = cls
        self.width = len(text) * COMMENT_CHAR_WIDTH + 10
        self.up = 8
        self.down = 8
        self.needsSpace = True
        addDebug(self)

    def __repr__(self) -> str:
        return f"Comment({repr(self.text)}, href={repr(self.href)}, title={repr(self.title)}, cls={repr(self.cls)})"

    def format(self, x: float, y: float, width: float) -> Comment:
        leftGap, rightGap = determineGaps(width, self.width)

        # Hook up the two sides if self is narrower than its stated width.
        Path(x, y).h(leftGap).addTo(self)
        Path(x + leftGap + self.width, y).h(rightGap).addTo(self)

        text = DiagramItem(
            "text",
            {"x": x + leftGap + self.width / 2, "y": y + 5, "class": "comment"},
            self.text,
        )
        if self.href is not None:
            a = DiagramItem("a", {"xlink:href": self.href}, text).addTo(self)
            text.addTo(a)
        else:
            text.addTo(self)
        if self.title is not None:
            DiagramItem("title", {}, self.title).addTo(self)
        return self

    def textDiagram(self) -> TextDiagram:
        # Note: href, title, and cls are ignored for text diagrams.
        return TextDiagram(0, 0, [self.text])


class Skip(DiagramItem):
    def __init__(self) -> None:
        DiagramItem.__init__(self, "g")
        self.width = 0
        self.up = 0
        self.down = 0
        addDebug(self)

    def format(self, x: float, y: float, width: float) -> Skip:
        Path(x, y).right(width).addTo(self)
        return self

    def textDiagram(self) -> TextDiagram:
        (line,) = TextDiagram._getParts(["line"])
        return TextDiagram(0, 0, [line])

    def __repr__(self) -> str:
        return "Skip()"


class TextDiagram:
    # Characters to use in drawing diagrams.  See setFormatting(), PARTS_ASCII, and PARTS_UNICODE.
    parts: Dict[str, str]

    def __init__(self, entry: int, exit: int, lines: List[str]) -> TextDiagram:
        # entry: The entry line for this diagram-part.
        self.entry: int = entry
        # exit: The exit line for this diagram-part.
        self.exit: int = exit
        # height: The height of this diagram-part, in lines.
        self.height: int = len(lines)
        # lines[]: The visual data of this diagram-part.  Each line must be the same length.
        self.lines: List[str] = lines.copy()
        # width: The width of this diagram-part, in character cells.
        self.width: int = len(lines[0]) if len(lines) > 0 else 0
        nl = "\n"  # f-strings can't contain \n until Python 3.12
        assert entry <= len(lines), f"Entry is not within diagram vertically:{nl}{self._dump(False)}"
        assert exit <= len(lines), f"Exit is not within diagram vertically:{nl}{self._dump(False)}"
        for i in range(0, len(lines)):
            assert len(lines[0]) == len(lines[i]), f"Diagram data is not rectangular:{nl}{self._dump(False)}"

    def alter(self, entry: int = None, exit: int = None, lines: List[str] = None) -> TextDiagram:
        """
        Create and return a new TextDiagram based on this instance, with the specified changes.

        Note: This is used sparingly, and may be a bad idea.
        """
        newEntry = entry or self.entry
        newExit = exit or self.exit
        newLines = lines or self.lines
        return self.__class__(newEntry, newExit, newLines.copy())

    def appendBelow(self, item: TextDiagram, linesBetween: List[str], moveEntry=False, moveExit=False) -> TextDiagram:
        """
        Create and return a new TextDiagram by appending the specified lines below this instance's data,
        and then appending the specified TextDiagram below those lines, possibly setting the resulting
        TextDiagram's entry and or exit indices to those of the appended item.
        """
        newWidth = max(self.width, item.width)
        newLines = []
        newLines += self.center(newWidth, " ").lines
        for line in linesBetween:
            newLines += [TextDiagram._padR(line, newWidth, " ")]
        newLines += item.center(newWidth, " ").lines
        newEntry = self.height + len(linesBetween) + item.entry if moveEntry else self.entry
        newExit = self.height + len(linesBetween) + item.exit if moveExit else self.exit
        newSelf = self.__class__(newEntry, newExit, newLines)
        return newSelf

    def appendRight(self, item: TextDiagram, charsBetween: str) -> TextDiagram:
        """
        Create and return a new TextDiagram by appending the specified TextDiagram to the right of this instance's data,
        aligning the left-hand exit and the right-hand entry points.  The charsBetween are inserted between the left-exit
        and right-entry, and equivalent spaces on all other lines.
        """
        joinLine = max(self.exit, item.entry)
        newHeight = max(self.height - self.exit, item.height - item.entry) + joinLine
        leftTopAdd = joinLine - self.exit
        leftBotAdd = newHeight - self.height - leftTopAdd
        rightTopAdd = joinLine - item.entry
        rightBotAdd = newHeight - item.height - rightTopAdd
        left = self.expand(0, 0, leftTopAdd, leftBotAdd)
        right = item.expand(0, 0, rightTopAdd, rightBotAdd)
        newLines = []
        for i in range(0, newHeight):
            sep = " " * len(charsBetween) if i != joinLine else charsBetween
            newLines += [(left.lines[i] + sep + right.lines[i])]
        newEntry = self.entry + leftTopAdd
        newExit = item.exit + rightTopAdd
        return self.__class__(newEntry, newExit, newLines)

    def center(self, width: int, pad: str) -> TextDiagram:
        """
        Create and return a new TextDiagram by centering the data of this instance within a new, equal or larger widtth.
        """
        assert width >= self.width, "Cannot center into smaller width"
        if width == self.width:
            return self.copy()
        else:
            total_padding = width - self.width
            leftWidth = total_padding // 2
            left = [(pad * leftWidth)] * self.height
            right = [(pad * (total_padding - leftWidth))] * self.height
            return self.__class__(self.entry, self.exit, TextDiagram._encloseLines(self.lines, left, right))

    def copy(self) -> TextDiagram:
        """
        Create and return a new TextDiagram by copying this instance's data.
        """
        return self.__class__(self.entry, self.exit, self.lines.copy())

    def expand(self, left: int, right: int, top: int, bottom: int) -> TextDiagram:
        """
        Create and return a new TextDiagram by expanding this instance's data by the specified amount in the specified directions.
        """
        assert left >= 0
        assert right >= 0
        assert top >= 0
        assert bottom >= 0
        if left + right + top + bottom == 0:
            return self.copy()
        else:
            line = self.parts["line"]
            newLines = []
            newLines += [(" " * (self.width + left + right))] * top
            for i in range(0, self.height):
                leftExpansion = line if i == self.entry else " "
                rightExpansion = line if i == self.exit else " "
                newLines += [(leftExpansion * left) + self.lines[i] + (rightExpansion * right)]
            newLines += [(" " * (self.width + left + right))] * bottom
            return self.__class__(self.entry + top, self.exit + top, newLines)

    @classmethod
    def rect(cls, item: Union[str, TextDiagram], dashed=False) -> TextDiagram:
        """
        Create and return a new TextDiagram for a rectangular box.
        """
        return cls._rectish("rect", item, dashed=dashed)

    @classmethod
    def roundrect(cls, item: Union[str, TextDiagram], dashed=False) -> TextDiagram:
        """
        Create and return a new TextDiagram for a rectangular box with rounded corners.
        """
        return cls._rectish("roundrect", item, dashed=dashed)

    @classmethod
    def setFormatting(cls, characters: Dict[str, str] = None, defaults: Dict[str, str] = None) -> None:
        """
        Set the characters to use for drawing text diagrams.
        """
        if characters is not None:
            cls.parts = {}
            if defaults is not None:
                cls.parts.update(defaults)
            cls.parts.update(characters)
        for name in cls.parts:
            assert len(cls.parts[name]) == 1, f"Text part {name} is more than 1 character: {cls.parts[name]}"

    def _dump(self, show=True) -> None:
        """
        Dump out the data of this instance for debugging, either displaying or returning it.
        DO NOT use this for actual work, only for debugging or in assertion output.
        """
        nl = "\n"  # f-strings can't contain \n until Python 3.12
        result = f"height={self.height}; len(lines)={len(self.lines)}"
        if self.entry > len(self.lines):
            result += f"; entry outside diagram: entry={self.entry}"
        if self.exit > len(self.lines):
            result += f"; exit outside diagram: exit={self.exit}"
        for y in range(0, max(len(self.lines), self.entry + 1, self.exit + 1)):
            result = result + f"{nl}[{y:03}]"
            if y < len(self.lines):
                result = result + f" '{self.lines[y]}' len={len(self.lines[y])}"
            if y == self.entry and y == self.exit:
                result += " <- entry, exit"
            elif y == self.entry:
                result += " <- entry"
            elif y == self.exit:
                result += " <- exit"
        if show:
            print(result)
        else:
            return result

    @classmethod
    def _encloseLines(cls, lines: List[str], lefts: List[str], rights: List[str]) -> List[str]:
        """
        Join the lefts, lines, and rights arrays together, line-by-line, and return the result.
        """
        assert len(lines) == len(lefts), "All arguments must be the same length"
        assert len(lines) == len(rights), "All arguments must be the same length"
        newLines = []
        for i in range(0, len(lines)):
            newLines.append(lefts[i] + lines[i] + rights[i])
        return newLines

    @staticmethod
    def _gaps(outerWidth: int, innerWidth: int) -> Tuple[int, int]:
        """
        Return the left and right pad spacing based on the alignment configuration setting.
        """
        diff = outerWidth - innerWidth
        if INTERNAL_ALIGNMENT == "left":
            return 0, diff
        elif INTERNAL_ALIGNMENT == "right":
            return diff, 0
        else:
            left = diff // 2
            right = diff - left
            return left, right

    @classmethod
    def _getParts(cls, partNames: List[str]) -> List[str]:
        """
        Return a list of text diagram drawing characters for the specified character names.
        """
        return [cls.parts[name] for name in partNames]

    @staticmethod
    def _maxWidth(*args: List[Union[int, str, List[str], TextDiagram]]) -> int:
        """
        Return the maximum width of all of the arguments.
        """
        maxWidth = 0
        for arg in args:
            if isinstance(arg, TextDiagram):
                width = arg.width
            elif isinstance(arg, list):
                width = max([len(e) for e in arg])
            elif isinstance(arg, int):
                width = len(str(arg))
            else:
                width = len(arg)
            maxWidth = width if width > maxWidth else maxWidth
        return maxWidth

    @staticmethod
    def _padL(string: str, width: int, pad: str) -> str:
        """
        Pad the specified string on the left to the specified width with the specified pad string and return the result.
        """
        assert (width - len(string)) % len(pad) == 0, f"Gap {width - len(string)} must be a multiple of pad string '{pad}'"
        return (pad * ((width - len(string) // len(pad)))) + string

    @staticmethod
    def _padR(string: str, width: int, pad: str) -> str:
        """
        Pad the specified string on the right to the specified width with the specified pad string and return the result.
        """
        assert (width - len(string)) % len(pad) == 0, f"Gap {width - len(string)} must be a multiple of pad string '{pad}'"
        return string + (pad * ((width - len(string) // len(pad))))

    @classmethod
    def _rectish(cls, rect_type: str, data: TextDiagram, dashed=False) -> TextDiagram:
        """
        Create and return a new TextDiagram for a rectangular box surrounding the specified TextDiagram, using the
        specified set of drawing characters (i.e., "rect" or "roundrect"), and possibly using dashed lines.
        """
        lineType = "_dashed" if dashed else ""
        topLeft, ctrLeft, botLeft, topRight, ctrRight, botRight, topHoriz, botHoriz, line, cross = cls._getParts([f"{rect_type}_top_left", f"{rect_type}_left{lineType}", f"{rect_type}_bot_left", f"{rect_type}_top_right", f"{rect_type}_right{lineType}", f"{rect_type}_bot_right", f"{rect_type}_top{lineType}", f"{rect_type}_bot{lineType}", "line", "cross"])
        itemWasFormatted = isinstance(data, TextDiagram)
        if itemWasFormatted:
            itemTD = data
        else:
            itemTD = TextDiagram(0, 0, [data])
        # Create the rectangle and enclose the item in it.
        lines = []
        lines += [(topHoriz * (itemTD.width + 2))]
        if itemWasFormatted:
            lines += itemTD.expand(1, 1, 0, 0).lines
        else:
            for i in range(0, len(itemTD.lines)):
                lines += [(" " + itemTD.lines[i] + " ")]
        lines += [(botHoriz * (itemTD.width + 2))]
        entry = itemTD.entry + 1
        exit = itemTD.exit + 1
        leftMaxWidth = cls._maxWidth(topLeft, ctrLeft, botLeft)
        lefts = [cls._padR(ctrLeft, leftMaxWidth, " ")] * len(lines)
        lefts[0] = cls._padR(topLeft, leftMaxWidth, topHoriz)
        lefts[-1] = cls._padR(botLeft, leftMaxWidth, botHoriz)
        if itemWasFormatted:
            lefts[entry] = cross
        rightMaxWidth = cls._maxWidth(topRight, ctrRight, botRight)
        rights = [cls._padL(ctrRight, rightMaxWidth, " ")] * len(lines)
        rights[0] = cls._padL(topRight, rightMaxWidth, topHoriz)
        rights[-1] = cls._padL(botRight, rightMaxWidth, botHoriz)
        if itemWasFormatted:
            rights[exit] = cross
        # Build the entry and exit perimeter.
        lines = TextDiagram._encloseLines(lines, lefts, rights)
        lefts = [" "] * len(lines)
        lefts[entry] = line
        rights = [" "] * len(lines)
        rights[exit] = line
        lines = TextDiagram._encloseLines(lines, lefts, rights)
        return cls(entry, exit, lines)

    def __repr__(self) -> str:
        return f"TextDiagram({self.entry}, {self.exit}, {self.lines})"

    # Note:  All the drawing sequences below MUST be single characters.  setFormatting() checks this.

    # Unicode 25xx box drawing characters, plus a few others.
    PARTS_UNICODE = {
        "cross_diag"             : "\u2573",
        "corner_bot_left"        : "\u2514",
        "corner_bot_right"       : "\u2518",
        "corner_top_left"        : "\u250c",
        "corner_top_right"       : "\u2510",
        "cross"                  : "\u253c",
        "left"                   : "\u2502",
        "line"                   : "\u2500",
        "line_vertical"          : "\u2502",
        "multi_repeat"           : "\u21ba",
        "rect_bot"               : "\u2500",
        "rect_bot_dashed"        : "\u2504",
        "rect_bot_left"          : "\u2514",
        "rect_bot_right"         : "\u2518",
        "rect_left"              : "\u2502",
        "rect_left_dashed"       : "\u2506",
        "rect_right"             : "\u2502",
        "rect_right_dashed"      : "\u2506",
        "rect_top"               : "\u2500",
        "rect_top_dashed"        : "\u2504",
        "rect_top_left"          : "\u250c",
        "rect_top_right"         : "\u2510",
        "repeat_bot_left"        : "\u2570",
        "repeat_bot_right"       : "\u256f",
        "repeat_left"            : "\u2502",
        "repeat_right"           : "\u2502",
        "repeat_top_left"        : "\u256d",
        "repeat_top_right"       : "\u256e",
        "right"                  : "\u2502",
        "roundcorner_bot_left"   : "\u2570",
        "roundcorner_bot_right"  : "\u256f",
        "roundcorner_top_left"   : "\u256d",
        "roundcorner_top_right"  : "\u256e",
        "roundrect_bot"          : "\u2500",
        "roundrect_bot_dashed"   : "\u2504",
        "roundrect_bot_left"     : "\u2570",
        "roundrect_bot_right"    : "\u256f",
        "roundrect_left"         : "\u2502",
        "roundrect_left_dashed"  : "\u2506",
        "roundrect_right"        : "\u2502",
        "roundrect_right_dashed" : "\u2506",
        "roundrect_top"          : "\u2500",
        "roundrect_top_dashed"   : "\u2504",
        "roundrect_top_left"     : "\u256d",
        "roundrect_top_right"    : "\u256e",
        "separator"              : "\u2500",
        "tee_left"               : "\u2524",
        "tee_right"              : "\u251c",
    }

    # Plain old ASCII characters.
    PARTS_ASCII = {
        "cross_diag"             : "X",
        "corner_bot_left"        : "\\",
        "corner_bot_right"       : "/",
        "corner_top_left"        : "/",
        "corner_top_right"       : "\\",
        "cross"                  : "+",
        "left"                   : "|",
        "line"                   : "-",
        "line_vertical"          : "|",
        "multi_repeat"           : "&",
        "rect_bot"               : "-",
        "rect_bot_dashed"        : "-",
        "rect_bot_left"          : "+",
        "rect_bot_right"         : "+",
        "rect_left"              : "|",
        "rect_left_dashed"       : "|",
        "rect_right"             : "|",
        "rect_right_dashed"      : "|",
        "rect_top_dashed"        : "-",
        "rect_top"               : "-",
        "rect_top_left"          : "+",
        "rect_top_right"         : "+",
        "repeat_bot_left"        : "\\",
        "repeat_bot_right"       : "/",
        "repeat_left"            : "|",
        "repeat_right"           : "|",
        "repeat_top_left"        : "/",
        "repeat_top_right"       : "\\",
        "right"                  : "|",
        "roundcorner_bot_left"   : "\\",
        "roundcorner_bot_right"  : "/",
        "roundcorner_top_left"   : "/",
        "roundcorner_top_right"  : "\\",
        "roundrect_bot"          : "-",
        "roundrect_bot_dashed"   : "-",
        "roundrect_bot_left"     : "\\",
        "roundrect_bot_right"    : "/",
        "roundrect_left"         : "|",
        "roundrect_left_dashed"  : "|",
        "roundrect_right"        : "|",
        "roundrect_right_dashed" : "|",
        "roundrect_top"          : "-",
        "roundrect_top_dashed"   : "-",
        "roundrect_top_left"     : "/",
        "roundrect_top_right"    : "\\",
        "separator"              : "-",
        "tee_left"               : "|",
        "tee_right"              : "|",
    }




# Default to Unicode box characters, they're much prettier than raw ASCII.
TextDiagram.setFormatting(TextDiagram.PARTS_UNICODE)

#if __name__ == "__main__":

if len(sys.argv) < 2 or sys.argv[1] == "":
        mode = "svg"
elif sys.argv[1].lower() in ["svg", "ascii", "unicode", "standalone"]:
        mode = sys.argv[1].lower()
else:
        raise ValueError(f"Unknown option: {sys.argv[1]}")
testList = sys.argv[2:]

def add(name: str, diagram: DiagramItem) -> None:
        if name in testList or len(testList) == 0:
            sys.stdout.write(f"\n<h3>{escapeHtml(name)}</h3>\n")
            if mode == "svg":
                diagram.writeSvg(sys.stdout.write)
            elif mode == "standalone":
                diagram.writeStandalone(sys.stdout.write)
            elif mode in ["ascii", "unicode"]:
                sys.stdout.write("\n<pre>\n")
                diagram.writeText(sys.stdout.write)
                sys.stdout.write("\n</pre>\n")
            sys.stdout.write("\n")

sys.stdout.write("<!doctype html><title>Test</title><body>")
if mode == "ascii":
        TextDiagram.setFormatting(TextDiagram.PARTS_ASCII)
elif mode == "unicode":
        TextDiagram.setFormatting(TextDiagram.PARTS_UNICODE)
elif mode in ("svg", "standalone"):
        sys.stdout.write(
            f"""
    		<style>
            {DEFAULT_STYLE}
    		.blue text {{ fill: blue; }}
    		</style>
    		"""
        )


with open(input_file+".py", "r", encoding="utf-8") as fh:
        print('\nConverting .py to .html', file=sys.__stdout__)
        exec(fh.read())  # pylint: disable=exec-used
sys.stdout.write("</body></html>")

print(f"\nConversion complete. Output saved to {input_file}.html", file=sys.__stdout__)