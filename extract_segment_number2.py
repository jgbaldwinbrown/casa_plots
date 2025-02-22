import re
import sys

def extract_with_regex(instream, outstream, ewasteregex, wasteregex, pureregex, segmentregex):
	for line in instream:
		stripped_line = line.rstrip("\n")

		ewastematch = ewasteregex.search(stripped_line)
		if ewastematch:
			outstream.write(stripped_line + " " + "ewaste" + "\n")
			continue

		wastematch = wasteregex.search(stripped_line)
		if wastematch:
			outstream.write(stripped_line + " " + "waste" + "\n")
			continue

		purematch = pureregex.search(stripped_line)
		if purematch:
			outstream.write(stripped_line + " " + "pure" + "\n")
			continue

		segmentmatch = segmentregex.search(stripped_line)
		if segmentmatch:
			eors = segmentmatch.group(2)
			if not eors:
				eors = segmentmatch.group(4)
			outstream.write(stripped_line + " " + eors.lower() + segmentmatch.group(6) + segmentmatch.group(7) + "\n")
			continue

		exit("This is impossible!")

def main():
	ewasteregex = re.compile("""[Ee][Ww]aste""")
	wasteregex = re.compile("""[Ww]aste""")
	pureregex = re.compile("""[Uu]nloaded|pure""")
	segmentregex = re.compile("""(([Ee])(xtracted)?|([Ss])(egment)?)([1-6])([Cc]?)""")
	extract_with_regex(sys.stdin, sys.stdout, ewasteregex, wasteregex, pureregex, segmentregex)

if __name__ == "__main__":
	main()
