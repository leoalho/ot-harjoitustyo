from tkinter import ttk

class NewProject():
    def __init__(self, root, mover, main_service) -> None:
        self._root = root
        self._main_service = main_service
        self._mover = mover
        self._frame = None
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        general_info = ttk.Label(master=self._frame, text="Enter a project name")
        self._entry = ttk.Entry(master=self._frame)
        create_user_button = ttk.Button(master=self._frame,
                            text="create project", command=self._create_project)
        cancel_button = ttk.Button(master=self._frame, text="cancel", command=self._cancel)
        general_info.grid(row=0, column=0, columnspan=2)
        self._entry.grid(row=1, column=0, columnspan=2)
        create_user_button.grid(row=2, column=0)
        cancel_button.grid(row=2, column=1)

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _create_project(self):
        project_name = self._entry.get()
        if project_name != "":
            self._main_service.create_project(project_name)
            from ui.views.projectView import ProjectView
            self._mover(ProjectView(self._root, self._mover, self._main_service))
    
    def _cancel(self):
        from ui.views.projectView import ProjectView
        self._mover(ProjectView(self._root, self._mover, self._main_service))