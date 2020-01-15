lines = ["<?xml version=\"1.0\" ?>",\
        "<testsuite errors=\"0\" failures=\"0\" name=\"Scenario_ConnexionDeconnexion\" tests=\"2\" time=\"10.842\">",
        "<testcase classname=\"Scenario_ConnexionDeconnexion\" name=\"Connexion\" time=\"2.554\"/>",
	    "<testcase classname=\"Scenario_ConnexionDeconnexion\" name=\"Deconnexion\" time=\"1.9\"/>",
        "</testsuite>"]

with open("D:\APPS\Jenkins\workspace\junit-sample\Output.xml", "w") as text_file:
    for line in lines :
        text_file.write(line)