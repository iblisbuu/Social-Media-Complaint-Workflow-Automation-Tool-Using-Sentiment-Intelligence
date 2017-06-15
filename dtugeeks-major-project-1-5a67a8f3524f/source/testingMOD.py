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

            def _qui():
                classifier.quit()  # stops mainloop
                classifier.destroy()

            bottom_fram = Frame(classifier)
            bottom_fram.grid(row=8, column=0, columnspan=2, sticky='w', pady=row_pady)
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
                a.plot([1, 2, 3, 4, 5],
                       [all_class[0], all_class[1], all_class[2])
                a.set_title('Accuracy Comparison')
                a.set_xlabel(
                    '1 - > Naive Bayes , 2 - > MultinomialNB, 3 - > BernoulliNB')
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