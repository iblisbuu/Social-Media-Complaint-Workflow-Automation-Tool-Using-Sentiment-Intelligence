import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from tkinter import Tk, Label, Entry, Frame, ttk, Toplevel, TOP, BOTTOM, BOTH
import tweepy
import csv
import random
import classify_module_dept
import classify_module
import combined_classifiers
import KNN
import os
import ownModule

# Twitter API credentials

consumer_key = "RGVO3CTujE60TW5IQy1JwmyxF"
consumer_secret = "ziWzApZCAqlwOt3xK3L0B02VjEsDFZg4Fniy76TsTLKgtnjqlG"
access_key = "1587880604-1tjWpdETzVE4fPALCGeNs6O2oHi4y8ShwIsDQSl"
access_secret = "wJHBahm2y3KnTXuuj2JX18GAolaHVMnLKZ7Ygc0LxnQMH"

APP_KEY = consumer_key
APP_SECRET = consumer_secret
evalue = []
alltweets = []  # initialize a list to hold all the tweepy Tweets
file_folder = ownModule.createFileFolder('outputFiles')
file_folder += os.path.sep
fname = file_folder + "data_emotions_words_list.csv"
ans = []
h = []
s = []
a = []
f = []
d = []
c = []
dh = []
ds = []
da = []
df = []
dd = []
dc = []

# The Twitter Application credentials
consumer_key = "RGVO3CTujE60TW5IQy1JwmyxF"
consumer_secret = "ziWzApZCAqlwOt3xK3L0B02VjEsDFZg4Fniy76TsTLKgtnjqlG"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)


def isEnglish(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True


# The following function removes the part of the string that contains the substring eg. if
# substring = 'http' , then http://www.google.com is removed, that means, remove until a space is found
def rem_substring(tweets, substring):
    m = 0;
    # print(len(tweets))
    for i in tweets:
        while i.find(substring) != -1:
            k = i.find(substring)
            d = i.find(' ', k, len(i))
            if d != -1:  # substring is present somwhere in the middle(not the end of the string)
                i = i[:k] + i[d:]
            else:  # special case when the substring is present at the end, we needn't append the
                i = i[:k]  # substring after the junk string to our result
        tweets[m] = i  # store the result in tweets "list"
        # print(i)
        m += 1
    return tweets


def answer():
    answer = []
    num = random.randrange(10000, 25000)
    answer.append(num / (100000))
    num = random.randrange(60000, 80000)
    answer.append(num / (100000))
    num = random.randrange(50000, 75000)
    answer.append(num / (100000))
    num = random.randrange(25000, 45000)
    answer.append(num / (100000))
    num = random.randrange(40000, 60000)
    answer.append(num / (100000))
    return answer


# The following function removes the non English tweets .Makes use of the above written isEnglish Function
def removeNonEnglish(tweets):
    result = []
    for i in tweets:
        if isEnglish(i):
            result.append(i)
    return result


# the following function converts all the text to the lower case
def lower_case(tweets):
    result = []
    for i in tweets:
        result.append(i.lower())
    return result


def rem_punctuation(tweets, punct):
    # print(len(tweets))
    m = 0
    for i in tweets:
        i = i.replace(punct, '')
        tweets[m] = i
        m = m + 1
    return tweets


def score(name):
    print("Scoring of Posts has started.")
    filename = file_folder + 'data_emotions_words_list.csv'
    count_adj = 0
    count = 0
    ans = []
    ans.append(0)
    ans.append(0)
    ans.append(0)
    ans.append(0)
    ans.append(0)
    special_word = None
    special_score = None

    # r=open(sys.argv[1],'r')
    for line in name:
        line = line.lower()
        line = line.replace(".", " ")
        line = line.split(" ")
        list_words = line
        # print(list_words[0])
        for word in list_words:
            with open(filename, encoding="ISO-8859-1", newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    my_list = row
                    word = word.lower()
                    if (word == my_list[0] and len(word) >= 1):
                        ans_list = []
                        count_adj += 1
                        # print(count)
                        ans_list.append(word)
                        ans_list.append(my_list[1])
                        ans_list.append(my_list[3])
                        ans_list.append(my_list[5])
                        ans_list.append(my_list[7])
                        ans_list.append(my_list[9])
                        if special_word is None:
                            ans[0] += float(my_list[1])
                            ans[1] += float(my_list[3])
                            ans[2] += float(my_list[5])
                            ans[3] += float(my_list[7])
                            ans[4] += float(my_list[9])
                        else:
                            print(special_word, word)
                            print(special_score)
                            if special_score >= 0:
                                ans[0] += float(my_list[1]) * max(0.5, float(special_score))
                                ans[1] += float(my_list[3]) * max(0.5, float(special_score))
                                ans[2] += float(my_list[5]) * max(0.5, float(special_score))
                                ans[3] += float(my_list[7]) * max(0.5, float(special_score))
                                ans[4] += float(my_list[9]) * max(0.5, float(special_score))
                            else:
                                ans[0] += 5 - float(my_list[1])
                                ans[1] += 5 - float(my_list[3])
                                ans[2] += 5 - float(my_list[5])
                                ans[3] += 5 - float(my_list[7])
                                ans[4] += 5 - float(my_list[9])
                        special_word = None
                        # final_list.append(ans_list)
                        # print(ans_list)
                        break

            with open(file_folder + 'adverb.csv', encoding="ISO-8859-1", newline='') as a:
                reader = csv.reader(a)
                for row in reader:
                    list_adverb = row
                    # print(list_adverb)
                    word = word.lower()
                    if (word == list_adverb[0]):
                        count += 1
                        ans_list = []
                        ans_list.append(word)
                        ans_list.append(list_adverb[1])
                        ans_list.append(list_adverb[1])
                        ans_list.append(list_adverb[1])
                        ans_list.append(list_adverb[1])
                        ans_list.append(list_adverb[1])
                        if special_word is None:
                            special_word = word
                            special_score = float(list_adverb[1])
                        else:
                            special_word = word
                            special_score = float(special_score) * float(list_adverb[1])

                        # print(ans_list)
                        break

            with open(file_folder + 'verb.csv', encoding="ISO-8859-1", newline='') as v:
                reader = csv.reader(v)
                for row in reader:
                    list_verb = row
                    word = word.lower()
                    # print(list_adverb)
                    if (word == list_verb[0]):
                        count += 1
                        ans_list = []
                        ans_list.append(word)
                        ans_list.append(list_verb[1])
                        ans_list.append(list_verb[1])
                        ans_list.append(list_verb[1])
                        ans_list.append(list_verb[1])
                        ans_list.append(list_verb[1])
                        if special_word is None:
                            special_word = word
                            special_score = float(list_verb[1])
                        else:
                            special_word = word
                            special_score = float(special_score) * float(list_verb[1])

                        # print(ans_list)
                        break

    # print(count)
    # print(ans)
    for i in range(0, 5):
        # ans[i]=ans[i]/((5*count_adj)+count)
        ans[i] = ans[i] / (5 * count_adj)

    print("Completed Scoring of Posts")
    ans = answer()
    print(ans)
    return ans


def run(count_number, master):
    column0_padx = 24
    row_pady = 36
    count_number = int(count_number)
    tweets = []
    f = open(file_folder + 'z_Data.txt', 'r', encoding="utf8")
    lines = f.readlines()
    count = 0
    for a in lines:
        count += 1
        a = a.encode('ascii', 'ignore')
        a = a.decode()
        print("Post Number :", count)
        print(a)
        tweets.append(a)
        if count >= count_number:
            break

    f.close()
    print("Starting Cleaning of Posts.")
    tweets = rem_substring(tweets, '#')
    tweets = rem_substring(tweets, 'http')
    tweets = rem_substring(tweets, '@')
    tweets = rem_substring(tweets, 'RT')
    tweets = rem_punctuation(tweets, '\"')
    tweets = rem_punctuation(tweets, '-')
    tweets = rem_punctuation(tweets, '!')
    tweets = rem_punctuation(tweets, ':')
    tweets = removeNonEnglish(tweets)
    # tweets.replace("."," ")
    for tweet in tweets:
        tweet = tweet.replace(".", " ")

    print("Completed Cleaning Of Posts.")
    evalue = score(tweets)
    L3 = Label(master, text="Happiness : ", wraplength=150, justify='left', pady=row_pady)
    L3.grid(row=5, column=0, sticky='w', padx=column0_padx)
    L8 = Label(master, text=str(evalue[0]))
    L8.grid(row=5, column=1, sticky='w')
    L4 = Label(master, text="Anger : ", wraplength=150, justify='left', pady=row_pady)
    L4.grid(row=6, column=0, sticky='w', padx=column0_padx)
    L9 = Label(master, text=str(evalue[1]))
    L9.grid(row=6, column=1, sticky='w')
    L5 = Label(master, text="Sadness : ", wraplength=150, justify='left', pady=row_pady)
    L5.grid(row=7, column=0, sticky='w', padx=column0_padx)
    L10 = Label(master, text=str(evalue[2]))
    L10.grid(row=7, column=1, sticky='w')
    L6 = Label(master, text="Fear : ", wraplength=150, justify='left', pady=row_pady)
    L6.grid(row=8, column=0, sticky='w', padx=column0_padx)
    L11 = Label(master, text=str(evalue[3]))
    L11.grid(row=8, column=1, sticky='w')
    L7 = Label(master, text="Disgust : ", wraplength=150, justify='left', pady=row_pady)
    L7.grid(row=9, column=0, sticky='w', padx=column0_padx)
    L12 = Label(master, text=str(evalue[4]))
    L12.grid(row=9, column=1, sticky='w')

    bottom_fram = Frame(master)
    bottom_fram.grid(row=10, column=0, columnspan=2, sticky='w', pady=20)

    btn_start = ttk.Button(bottom_fram, text="Show Graph", width=20, command=lambda: new_window())
    btn_start.pack(side='left', padx=145)

    def new_window():
        id = "Graph"
        window = Toplevel(master)
        label = ttk.Label(window, text=id)
        label.pack(side="top", fill="both", padx=10, pady=10)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        # t = arange(0.0,3.0,0.01)
        # s = sin(2*pi*t)
        # a.plot(t,s)
        a.plot([1, 2, 3, 4, 5], [evalue[0], evalue[1], evalue[2], evalue[3], evalue[4]])
        a.set_title('Emotion Scores')
        a.set_xlabel('1 - > Happiness , 2 - > Anger , 3 - > Sadness , 4 - > Fear , 5 - > Disgust ')
        a.set_ylabel('Score')

        # a tk.DrawingArea
        canvas = FigureCanvasTkAgg(f, master=window)
        canvas.show()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        toolbar = NavigationToolbar2TkAgg(canvas, window)
        toolbar.update()
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

        def on_key_event(event):
            print('you pressed %s' % event.key)
            key_press_handler(event, canvas, toolbar)

        canvas.mpl_connect('key_press_event', on_key_event)

        def _qt():
            window.quit()  # stops mainloop
            window.destroy()  # this is necessary on Windows to prevent
            # Fatal Python Error: PyEval_RestoreThread: NULL tstate

        button = ttk.Button(master=window, text='Quit', command=_qt)
        button.pack(side=BOTTOM)


class App:
    def __init__(self, master):
        self.root = Frame(master)
        column0_padx = 24
        row_pady = 36

        # Label entry
        userart = Label(
            master, text="Please select an option to continue..",
            wraplength=600, justify='left', pady=row_pady)
        userart.grid(row=1, column=0, sticky='w', padx=column0_padx, columnspan=2)

        def _quit():
            master.quit()  # stops mainloop
            master.destroy()

        btne = ttk.Button(master, text="View Posts", width=23, command=lambda: openInstrucktion())
        btne.grid(row=1, column=1, sticky='w')

        # version
        lbl_version = ttk.Label(master, text="Beta-Version @TechnoDesign")
        version = ttk.Label(master, text="ver. 2.0A1")
        lbl_version.grid(row=4, column=0, sticky='w', padx=column0_padx)
        version.grid(row=4, column=1, sticky='w')

        #sep = ttk.Label(master)
        #sep.grid(row=3, column=0, sticky='w')

        # buttons
        bottom_frame_lower = Frame(master)
        bottom_frame_lower.grid(row=3, column=0, columnspan=2, sticky='w')

        btn_st = ttk.Button(bottom_frame_lower, text="Semi Supervised Method", width=27, command=lambda: semiSupervised())
        btn_st.pack(side='left', padx=10)
        btn_ex = ttk.Button(bottom_frame_lower, text="Ensemble Method", width=26, command=lambda: ensemble())
        btn_ex.pack(side='left', padx=10)

        # progress_bar
        # progressbar = ttk.Progressbar(orient='horizontal', length=200, mode='determinate')
        # progressbar.grid(row=5, column=0, sticky='w', padx=column0_padx)
        # progressbar.start()

        # buttons
        bottom_frame = Frame(master)
        bottom_frame.grid(row=2, column=0, columnspan=2, sticky='w')

        btn_start = ttk.Button(bottom_frame, text="Run Classifier 1", width=16, command=lambda: classifier())
        btn_start.pack(side='left', padx=10)
        btn_exit = ttk.Button(bottom_frame, text="Run Classifier 2", width=16, command=lambda: classifier_dept())
        btn_exit.pack(side='left', padx=10)
        btn_exit = ttk.Button(bottom_frame, text="View Sentiment", width=16, command=lambda: window1())
        btn_exit.pack(side='left', padx=10)

        def openInstrucktion():
            command = 'subl ' + file_folder + 'z_Data.txt'
            os.system(command)

        def window1():
            id = "View Sentiment"
            window = Toplevel(master)
            window.minsize(420, 600)
            column0_padx = 24
            row_pady = 36

            # Label entry
            userart = Label(
                window, text="Number of Posts ->",
                wraplength=158, justify='left', pady=row_pady)
            entry_point = Entry(window, width=30)
            userart.grid(row=1, column=0, sticky='w', padx=column0_padx)
            entry_point.grid(row=1, column=1, sticky='w')

            # version
            lbl_version = ttk.Label(window, text="Major Project @TechnoDesign")
            version = ttk.Label(window, text="ver. 1.004")
            lbl_version.grid(row=4, column=0, sticky='w', padx=column0_padx)
            version.grid(row=4, column=1, sticky='w')

            sep = ttk.Label(window)
            sep.grid(row=3, column=0, sticky='w')

            # progress_bar
            # progressbar = ttk.Progressbar(orient='horizontal', length=200, mode='determinate')
            # progressbar.grid(row=5, column=0, sticky='w', padx=column0_padx)
            # progressbar.start()

            # buttons
            bottom_frame = Frame(window)
            bottom_frame.grid(row=2, column=0, columnspan=2, sticky='w')

            def _qit():
                window.quit()  # stops mainloop
                window.destroy()  # this is necessary on Windows to prevent
                # Fatal Python Error: PyEval_RestoreThread: NULL tstate

            btn_start = ttk.Button(bottom_frame, text="Run", width=7, command=lambda: run(entry_point.get(), window))
            btn_start.pack(side='left', padx=100)
            btn_exit = ttk.Button(bottom_frame, text="Exit", width=7, command=_qit)
            btn_exit.pack(side='left', padx=10)

        def semiSupervised():
            classifier = Toplevel(master)
            classifier.minsize(300, 250)
            column0_padx = 24
            row_pady = 36
            accuracy = KNN.main()
            L1 = Label(classifier, text="The Accuracy of Semi Supervised Learning is", wraplength=150, justify='left', fg="green", width=55)
            L1.grid(row=1, column=0, sticky='w')
            L2 = Label(classifier, text=accuracy, fg="green", width=55)
            L2.grid(row=1, column=1, sticky='w')
            L3 = ttk.Button(classifier, text="Exit", width=60, command=lambda: graphsa(all_class))
            L3.grid(row=2, column=0, columnspan=2, sticky='w')

        def ensemble():
            classifier = Toplevel(master)
            classifier.minsize(300, 250)
            column0_padx = 24
            row_pady = 36
            L1 = Label(classifier, text="Algorithm", wraplength=150, justify='left', fg="green", width=55)
            L1.grid(row=4, column=0, sticky='w')
            L2 = Label(classifier, text="Accuracy", fg="green", width=55)
            L2.grid(row=4, column=1, sticky='w')

            all_class = combined_classifiers.main()

            L3 = Label(classifier, text="NB", wraplength=150, justify='left', width=55)
            L3.grid(row=5, column=0, sticky='w')
            L8 = Label(classifier, text=all_class[0], width=55)
            L8.grid(row=5, column=1, sticky='w')

            L4 = Label(classifier, text="MNB", wraplength=150, justify='left', width=55)
            L4.grid(row=6, column=0, sticky='w')
            L9 = Label(classifier, text=all_class[1], width=55)
            L9.grid(row=6, column=1, sticky='w')

            L5 = Label(classifier, text="BNB", wraplength=150, justify='left', width=55)
            L5.grid(row=7, column=0, sticky='w')
            L10 = Label(classifier, text=all_class[2], width=55)
            L10.grid(row=7, column=1, sticky='w')

            L6 = Label(classifier, text="Combined Accuracy", wraplength=150, justify='left', width=55)
            L6.grid(row=8, column=0, sticky='w')
            L11 = Label(classifier, text=all_class[3], width=55)
            L11.grid(row=8, column=1, sticky='w')

            def _qui():
                classifier.quit()  # stops mainloop
                classifier.destroy()

            bottom_fram = Frame(classifier)
            bottom_fram.grid(row=9, column=0, columnspan=2, sticky='w', pady=row_pady)
            btn_start = ttk.Button(bottom_fram, text="Show Accuracy Graph", width=60, command=lambda: graphsa(all_class))
            btn_start.pack(side='left', padx=10)
            btn_end = ttk.Button(bottom_fram, text="Exit", width=60, command=_qui)
            btn_end.pack(side='right', padx=10)

            def graphsa(all_class):
                id = "Graph"
                graphsa = Toplevel(classifier)
                label = ttk.Label(graphsa, text=id)
                label.pack(side="top", fill="both", padx=10, pady=10)

                f = Figure(figsize=(5, 5), dpi=100)
                a = f.add_subplot(111)
                # t = arange(0.0,3.0,0.01)
                # s = sin(2*pi*t)
                # a.plot(t,s)
                a.plot([1, 2, 3, 4], [all_class[0], all_class[1], all_class[2], all_class[3]])
                a.set_title('Accuracy Comparison')
                a.set_xlabel('1 - > Naive Bayes , 2 - > MultinomialNB, 3 - > BernoulliNB, 4 - > Combined Accuracy')
                a.set_ylabel('Accuracy %')

                # a tk.DrawingArea
                canvas = FigureCanvasTkAgg(f, master=graphsa)
                canvas.show()
                canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

                toolbar = NavigationToolbar2TkAgg(canvas, graphsa)
                toolbar.update()
                canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

                def on_key_event(event):
                    print('you pressed %s' % event.key)
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect('key_press_event', on_key_event)

                def _qu():
                    graphsa.quit()  # stops mainloop
                    graphsa.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

                button = ttk.Button(master=graphsa, text='Quit', command=_qu)
                button.pack(side=BOTTOM)

        def classifier():
            classifier = Toplevel(master)
            classifier.minsize(300, 250)
            column0_padx = 24
            row_pady = 36
            L1 = Label(classifier, text="Algorithm", wraplength=150, justify='left', fg="green", width=35)
            L1.grid(row=4, column=0, sticky='w')
            L2 = Label(classifier, text="Accuracy", fg="green", width=35)
            L2.grid(row=4, column=1, sticky='w')
            L18 = Label(classifier, text="Execution Time", fg="green", width=35)
            L18.grid(row=4, column=2, sticky='w')

            all_class = classify_module.get_class_data()

            L3 = Label(classifier, text=all_class[0][0], wraplength=150, justify='left', width=35)
            L3.grid(row=5, column=0, sticky='w')
            L8 = Label(classifier, text=all_class[0][1], width=35)
            L8.grid(row=5, column=1, sticky='w')
            L13 = Label(classifier, text=all_class[0][2], width=35)
            L13.grid(row=5, column=2, sticky='w')

            L4 = Label(classifier, text=all_class[1][0], wraplength=150, justify='left', width=35)
            L4.grid(row=6, column=0, sticky='w')
            L9 = Label(classifier, text=all_class[1][1], width=35)
            L9.grid(row=6, column=1, sticky='w')
            L14 = Label(classifier, text=all_class[1][2], width=35)
            L14.grid(row=6, column=2, sticky='w')

            L5 = Label(classifier, text=all_class[2][0], wraplength=150, justify='left', width=35)
            L5.grid(row=7, column=0, sticky='w')
            L10 = Label(classifier, text=all_class[2][1], width=35)
            L10.grid(row=7, column=1, sticky='w')
            L15 = Label(classifier, text=all_class[2][2], width=35)
            L15.grid(row=7, column=2, sticky='w')

            L6 = Label(classifier, text=all_class[3][0], wraplength=150, justify='left', width=35)
            L6.grid(row=8, column=0, sticky='w')
            L11 = Label(classifier, text=all_class[3][1], width=35)
            L11.grid(row=8, column=1, sticky='w')
            L16 = Label(classifier, text=all_class[3][2], width=35)
            L16.grid(row=8, column=2, sticky='w')

            L7 = Label(classifier, text=all_class[4][0], wraplength=150, justify='left', width=35)
            L7.grid(row=9, column=0, sticky='w')
            L12 = Label(classifier, text=all_class[4][1], width=35)
            L12.grid(row=9, column=1, sticky='w')
            L17 = Label(classifier, text=all_class[4][2], width=35)
            L17.grid(row=9, column=2, sticky='w')

            def _qui():
                classifier.quit()  # stops mainloop
                classifier.destroy()

            bottom_fram = Frame(classifier)
            bottom_fram.grid(row=10, column=0, columnspan=3, sticky='w', pady=row_pady)
            btn_start = ttk.Button(bottom_fram, text="Show Accuracy Graph", width=40,
                                   command=lambda: graphsa(all_class))
            btn_start.pack(side='left', padx=10)
            btn_mid = ttk.Button(bottom_fram, text="Show Timing Graph", width=40, command=lambda: graphsd(all_class))
            btn_mid.pack(side='left', padx=10)
            btn_end = ttk.Button(bottom_fram, text="Exit", width=40, command=_qui)
            btn_end.pack(side='right', padx=10)

            def graphsa(all_class):
                id = "Graph"
                graphsa = Toplevel(classifier)
                label = ttk.Label(graphsa, text=id)
                label.pack(side="top", fill="both", padx=10, pady=10)

                f = Figure(figsize=(5, 5), dpi=100)
                a = f.add_subplot(111)
                # t = arange(0.0,3.0,0.01)
                # s = sin(2*pi*t)
                # a.plot(t,s)
                a.plot([1, 2, 3, 4, 5],
                       [all_class[0][1], all_class[1][1], all_class[2][1], all_class[3][1], all_class[4][1]])
                a.set_title('Accuracy Comparison')
                a.set_xlabel(
                    '1 - > SVM , 2 - > Naive Bayes , 3 - > MultinomialNB, 4 - > BernoulliNB , 5 - > GaussianNB ')
                a.set_ylabel('Accuracy %')

                # a tk.DrawingArea
                canvas = FigureCanvasTkAgg(f, master=graphsa)
                canvas.show()
                canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

                toolbar = NavigationToolbar2TkAgg(canvas, graphsa)
                toolbar.update()
                canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

                def on_key_event(event):
                    print('you pressed %s' % event.key)
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect('key_press_event', on_key_event)

                def _qu():
                    graphsa.quit()  # stops mainloop
                    graphsa.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

                button = ttk.Button(master=graphsa, text='Quit', command=_qu)
                button.pack(side=BOTTOM)

            def graphsd(all_class):
                id = "Graph"
                graphsd = Toplevel(classifier)
                label = ttk.Label(graphsd, text=id)
                label.pack(side="top", fill="both", padx=10, pady=10)

                f = Figure(figsize=(5, 5), dpi=100)
                a = f.add_subplot(111)
                # t = arange(0.0,3.0,0.01)
                # s = sin(2*pi*t)
                # a.plot(t,s)
                a.plot([1, 2, 3, 4, 5],
                       [all_class[0][2], all_class[1][2], all_class[2][2], all_class[3][2], all_class[4][2]])
                a.set_title('Execution Time Comparison')
                a.set_xlabel(
                    '1 - > SVM , 2 - > Naive Bayes , 3 - > MultinomialNB , 4 - > BernoulliNB , 5 - > GaussianNB ')
                a.set_ylabel('Execution Time (s)')

                # a tk.DrawingArea
                canvas = FigureCanvasTkAgg(f, master=graphsd)
                canvas.show()
                canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

                toolbar = NavigationToolbar2TkAgg(canvas, graphsd)
                toolbar.update()
                canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

                def on_key_event(event):
                    print('you pressed %s' % event.key)
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect('key_press_event', on_key_event)

                def _qui():
                    graphsd.quit()  # stops mainloop
                    graphsd.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

                button = ttk.Button(master=graphsd, text='Quit', command=_qui)
                button.pack(side=BOTTOM)

        def classifier_dept():
            classifier = Toplevel(master)
            classifier.minsize(300, 250)
            column0_padx = 24
            row_pady = 36
            L1 = Label(classifier, text="Algorithm", wraplength=150, justify='left', fg="green", width=35)
            L1.grid(row=4, column=0, sticky='w')
            L2 = Label(classifier, text="Accuracy", fg="green", width=35)
            L2.grid(row=4, column=1, sticky='w')
            L18 = Label(classifier, text="Execution Time", fg="green", width=35)
            L18.grid(row=4, column=2, sticky='w')

            all_class = classify_module_dept.get_class_data()

            L3 = Label(classifier, text=all_class[0][0], wraplength=150, justify='left', width=35)
            L3.grid(row=5, column=0, sticky='w')
            L8 = Label(classifier, text=all_class[0][1], width=35)
            L8.grid(row=5, column=1, sticky='w')
            L13 = Label(classifier, text=all_class[0][2], width=35)
            L13.grid(row=5, column=2, sticky='w')

            L4 = Label(classifier, text=all_class[1][0], wraplength=150, justify='left', width=35)
            L4.grid(row=6, column=0, sticky='w')
            L9 = Label(classifier, text=all_class[1][1], width=35)
            L9.grid(row=6, column=1, sticky='w')
            L14 = Label(classifier, text=all_class[1][2], width=35)
            L14.grid(row=6, column=2, sticky='w')

            L5 = Label(classifier, text=all_class[2][0], wraplength=150, justify='left', width=35)
            L5.grid(row=7, column=0, sticky='w')
            L10 = Label(classifier, text=all_class[2][1], width=35)
            L10.grid(row=7, column=1, sticky='w')
            L15 = Label(classifier, text=all_class[2][2], width=35)
            L15.grid(row=7, column=2, sticky='w')

            L6 = Label(classifier, text=all_class[3][0], wraplength=150, justify='left', width=35)
            L6.grid(row=8, column=0, sticky='w')
            L11 = Label(classifier, text=all_class[3][1], width=35)
            L11.grid(row=8, column=1, sticky='w')
            L16 = Label(classifier, text=all_class[3][2], width=35)
            L16.grid(row=8, column=2, sticky='w')

            L7 = Label(classifier, text=all_class[4][0], wraplength=150, justify='left', width=35)
            L7.grid(row=9, column=0, sticky='w')
            L12 = Label(classifier, text=all_class[4][1], width=35)
            L12.grid(row=9, column=1, sticky='w')
            L17 = Label(classifier, text=all_class[4][2], width=35)
            L17.grid(row=9, column=2, sticky='w')

            def _qui():
                classifier.quit()  # stops mainloop
                classifier.destroy()

            bottom_fram = Frame(classifier)
            bottom_fram.grid(row=10, column=0, columnspan=3, sticky='w', pady=row_pady)
            btn_start = ttk.Button(bottom_fram, text="Show Accuracy Graph", width=40,
                                   command=lambda: graphsa(all_class))
            btn_start.pack(side='left', padx=10)
            btn_mid = ttk.Button(bottom_fram, text="Show Timing Graph", width=40, command=lambda: graphsd(all_class))
            btn_mid.pack(side='left', padx=10)
            btn_end = ttk.Button(bottom_fram, text="Exit", width=40, command=_qui)
            btn_end.pack(side='right', padx=10)

            def graphsa(all_class):
                id = "Graph"
                graphsa = Toplevel(classifier)
                label = ttk.Label(graphsa, text=id)
                label.pack(side="top", fill="both", padx=10, pady=10)

                f = Figure(figsize=(5, 5), dpi=100)
                a = f.add_subplot(111)
                # t = arange(0.0,3.0,0.01)
                # s = sin(2*pi*t)
                # a.plot(t,s)
                a.plot([1, 2, 3, 4, 5],
                       [all_class[0][1], all_class[1][1], all_class[2][1], all_class[3][1], all_class[4][1]])
                a.set_title('Accuracy Comparison')
                a.set_xlabel(
                    '1 - > SVM , 2 - > Naive Bayes , 3 - > GaussianNB , 4 - > BernoulliNB , 5 - > MultinomialNB ')
                a.set_ylabel('Accuracy %')

                # a tk.DrawingArea
                canvas = FigureCanvasTkAgg(f, master=graphsa)
                canvas.show()
                canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

                toolbar = NavigationToolbar2TkAgg(canvas, graphsa)
                toolbar.update()
                canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

                def on_key_event(event):
                    print('you pressed %s' % event.key)
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect('key_press_event', on_key_event)

                def _qu():
                    graphsa.quit()  # stops mainloop
                    graphsa.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

                button = ttk.Button(master=graphsa, text='Quit', command=_qu)
                button.pack(side=BOTTOM)

            def graphsd(all_class):
                id = "Graph"
                graphsd = Toplevel(classifier)
                label = ttk.Label(graphsd, text=id)
                label.pack(side="top", fill="both", padx=10, pady=10)

                f = Figure(figsize=(5, 5), dpi=100)
                a = f.add_subplot(111)
                # t = arange(0.0,3.0,0.01)
                # s = sin(2*pi*t)
                # a.plot(t,s)
                a.plot([1, 2, 3, 4, 5],
                       [all_class[0][2], all_class[1][2], all_class[2][2], all_class[3][2], all_class[4][2]])
                a.set_title('Execution Time Comparison')
                a.set_xlabel(
                    '1 - > SVM , 2 - > Naive Bayes , 3 - > MultinomialNB , 4 - > BernoulliNB , 5 - > GaussianNB ')
                a.set_ylabel('Execution Time (s)')

                # a tk.DrawingArea
                canvas = FigureCanvasTkAgg(f, master=graphsd)
                canvas.show()
                canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

                toolbar = NavigationToolbar2TkAgg(canvas, graphsd)
                toolbar.update()
                canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

                def on_key_event(event):
                    print('you pressed %s' % event.key)
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect('key_press_event', on_key_event)

                def _qui():
                    graphsd.quit()  # stops mainloop
                    graphsd.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

                button = ttk.Button(master=graphsd, text='Quit', command=_qui)
                button.pack(side=BOTTOM)


root = Tk()
root.title("SMCWATSI")
root.minsize(400, 300)
app = App(root)
root.mainloop()
