def cypher(content):
    i = "\ "
	i = i.replace(" ", "")
	content = content.lower().replace("a", "01 ")
	content = content.replace("l", "02 ")
	content = content.replace("c", "03 ")
	content = content.replace("b", "04 ")
	content = content.replace("s", "05 ")
	content = content.replace("f", "06 ")
	content = content.replace("q", "07 ")
	content = content.replace("d", "08 ")
	content = content.replace("g", "09 ")
	content = content.replace("j", "10 ")
	content = content.replace("k", "11 ")
	content = content.replace("y", "12 ")
	content = content.replace("e", "13 ")
	content = content.replace("p", "14 ")
	content = content.replace("o", "15 ")
	content = content.replace("i", "16 ")
	content = content.replace("m", "17 ")
	content = content.replace("n", "18 ")
	content = content.replace("v", "19 ")
	content = content.replace("x", "20 ")
	content = content.replace("z", "21 ")
	content = content.replace("u", "22 ")
	content = content.replace("r", "23 ")
	content = content.replace("w", "24 ")
	content = content.replace("t", "25 ")
	content = content.replace("h", "26 ")
	content = content.replace("1", "ox ")
	content = content.replace("6", "ms ")
	content = content.replace("2", "xz ")
	content = content.replace("5", "hg ")
	content = content.replace("8", "aw ")
	content = content.replace("7", "lc ")
	content = content.replace("4", "qd ")
	content = content.replace("9", "gs ")
	content = content.replace("3", "bn ")
	content = content.replace("0", "op ")
	content = content.replace("!", "37 ")
	content = content.replace("@", "38 ")
	content = content.replace("#", "39 ")
	content = content.replace("%", "40 ")
	content = content.replace("$", "41 ")
	content = content.replace("^", "42 ")
	content = content.replace("&", "43 ")
	content = content.replace("*", "44 ")
	content = content.replace("(", "71 ")
	content = content.replace(")", "72 ")
	content = content.replace("[", "45 ")
	content = content.replace("]", "46 ")
	content = content.replace("-", "47 ")
	content = content.replace("_", "48 ")
	content = content.replace("=", "49 ")
	content = content.replace("+", "50 ")
	content = content.replace("`", "51 ")
	content = content.replace("~", "52 ")
	content = content.replace(".", "53 ")
	content = content.replace(",", "54 ")
	content = content.replace("<", "55 ")
	content = content.replace(">", "56 ")
	content = content.replace("?", "57 ")
	content = content.replace("/", "58 ")
	content = content.replace(i, "59 ")
	content = content.replace(";", "60 ")
	content = content.replace(":", "61 ")
	content = content.replace("'", "62 ")
	content = content.replace('"', "63 ")
	content = content.replace(" ", "-")
	content = content[:-1]
	return content