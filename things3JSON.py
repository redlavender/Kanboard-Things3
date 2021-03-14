import json
import sqlite3

class Things3JSON():

    def __init__(self,￼kanban_data, things_kanboard_dictionary={}, things_action="create")
        #things_action is "create" which is the default if left blank or "update"
        #kanban_data is the json of the kanboard kanban
        #things_kanboard_dictionary is the json of the kanboard to things3 mapping
        

        #self.id = ""
        #self.title = ""
        #self.notes = ""
        #'''self.prependNotes = ""
        #'''self.appendNotes = ""
        #self.when = ""
        #self.deadline = ""
        #self.tagIDs = []
        #self.tags = []
        #'''self.addTags = []
        #self.checklistItems = []
        #'''self.prependChecklistItems = []
        #'''self.appendChecklistItems = []
        #self.listID = ""
        #self.list = ""
        #self.heading = ""
        #self.completed = ""
        #self.canceled = ""
        #self.creationDate = ""
        #self.completionDate = ""

        self.things3json = {}
        self.things3json["title"] = kanban_data["title"]
        self.things3json["notes"] = "kanban ID - " + kanban_data["id"]
        self.things3json["when"] = "anytime"
        self.things3json["deadline"] = ""
        self.things3json["tags"] = []
        #print(self.things3json["tags"])
        #print(kanban_data["column"]["title"])
        self.things3json["tags"].append(kanban_data["column"]["title"])
        #print(self.things3json["tags"])
        for key in kanban_data["tags"]:
            #print(kanban_data["tags"][key])
            #print(self.things3json["tags"])
            self.things3json["tags"].append(kanban_data["tags"][key])
        self.things3json["checklist-items"] = []
        self.things3json["list-id"] = ""
        self.things3json["list"] = ""
        self.things3json["heading"] = ""
        self.things3json["completed"] = False
        self.things3json["canceled"] = False
        self.things3json["creation-date"] = kanban_data["date_creation"]
        self.things3json["completion-date"] = ""