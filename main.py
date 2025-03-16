from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Web Builder Plugin is running!"}

@app.get("/check_installed_services")
def check_installed_services(projectId: str):
    return {"projectId": projectId, "installed_services": ["Cloud Run", "Firestore"]}

@app.post("/deploy_website")
def deploy_website(projectId: str, hostingService: str):
    return {"message": f"Website deployed on {hostingService} for project {projectId}"}

@app.post("/estimate_cloud_costs")
def estimate_cloud_costs(hostingType: str, databaseType: str):
    return {"estimated_cost": "$85 per month"}