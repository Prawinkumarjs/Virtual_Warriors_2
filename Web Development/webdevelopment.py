from nicegui import app,run,ui
# use to make connection
@ui.page("/")
def homepage():
    ui.card()
    ui.button(text="Next Page",on_click=lambda:ui.navigate.to('/nextpage'),color="Red")
    ui.label("Vankam da Mapla... Home Page la irunthu")
    
@ui.page('/nextpage')
def nextpage():
    ui.button("Previous Page",on_click=lambda:ui.navigate.to('/'))
    ui.label("Vankam da Mapla... Next Page la irunthu")
    
ui.run(host="0.0.0.0",port=5000)