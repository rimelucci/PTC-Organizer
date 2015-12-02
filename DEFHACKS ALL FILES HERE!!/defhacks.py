from flask import Flask, render_template, request

joe = Flask(__name__)


@joe.route( "/" )
def index():
    # return "<form 
    return render_template("base.html")


def getemptytimes(subj, teach):
    timetable = open(subj + "/" + teach + ".csv", "r").readlines()
    for i in timetable:
        i = i.split(',')

    emptytimes = []
    for x in timetable:
        #print timetable
        print x
        x = x.split(',')
        if x[1] == 'false':
            emptytimes.append(x[0])
            print x
            # + "deLIMITER"
    s = """<select name = "time" id="time">
                    <option "" disabled selected>--Select Time--</option>"""
    print emptytimes
    for y in emptytimes:
        
        s += '<option value=' + y + '>' + y + '</option>'
    s += "</select>"
    s += '<input type="hidden" name="subject" value="'
    s += subj + '">'
    s += "</select>"
    s += '<input type="hidden" name="teacher" value="'
    s += teach +'">'
     
        
    return s

@joe.route("/music.txt")
def music():
    return  open("music.txt", "r").read()

@joe.route("/english.txt")
def english():
    return  open("english.txt", "r").read()

@joe.route("/health.txt")
def health():
    return  open("health.txt", "r").read()

@joe.route("/pe.txt")
def pe():
    return  open("pe.txt", "r").read()

@joe.route("/cs.txt")
def cs():
    return  open("cs.txt", "r").read()

@joe.route("/chem.txt")
def chem():
    return  open("chem.txt", "r").read()

@joe.route("/bio.txt")
def bio():
    return  open("bio.txt", "r").read()

@joe.route("/physics.txt")
def physics():
    return  open("physics.txt", "r").read()

@joe.route("/lang.txt")
def lang():
    return  open("lang.txt", "r").read()

@joe.route("/ss.txt")
def ss():
    return  open("ss.txt", "r").read()

@joe.route("/math.txt")
def math():
    return  open("math.txt", "r").read()

@joe.route("/tech.txt")
def tech():
    return  open("tech.txt", "r").read()

@joe.route("/art.txt")
def art():
    return  open("art.txt", "r").read()



@joe.route( "/teacherPage", methods = ["GET", "POST"] )
def form():
    if request.method == "GET":
        teach = request.args.get('teacher', '')
        subj = request.args.get('subject', '')
        availableslots = getemptytimes(subj, teach)
        s = ""
        for i in availableslots:
            s += i
        x = fillTable(teach, subj)
        y = getemptytimes(subj, teach)
        return render_template("techtable.html", s=x, t=y)
    else:
	return "idfk"


def fillTable(teach, subj):
    timetable = open(subj + "/" + teach + ".csv", "r").readlines()
    for i in timetable:
        i = i.split(',')
    s = ""
    for x in timetable:
        x = x.split(',')
        s += '<tr> <td class="table1">' 
        s += x[0]
        s += "</td> \n \t <td class='table1'>"
        s += x[2] + "</td>  <td class='table1'>"
        s += x[3] + "</td> </tr>"
    return s  
   

def changeline(filename, time, newtext):
    print "WTF HAAAAAAAALP" + newtext
    lines = open(filename, 'r').readlines()
    index = 0
    fullFile = ""
    for a in lines:
        s = a
        s = s.split(',')
        if s[0] == time:
            fullFile += newtext + "\n"
        else:
            fullFile += a
            index += 1
    
    outStream = open(filename, "w")
    outStream.write(fullFile)
    outStream.close()
    

@joe.route( "/successPage", methods = ["GET", "POST"])
def successPage():
    if request.method == "GET":

        teach = request.args.get('teacher', '')
        subj = request.args.get('subject', '')
        
        file = "" + subj + "/" + teach + ".csv"
        
        time = request.args.get('time', '')
        name = request.args.get('parentName', '')
        student = request.args.get('studentName', '')

        newline = "" + time + "," + "true" + "," + name + "," + student 
        
        changeline(file, time, newline)
        
        return render_template("base.html")


if __name__ == "__main__":
            
    joe.debug = True
    
    joe.run()
    


            
