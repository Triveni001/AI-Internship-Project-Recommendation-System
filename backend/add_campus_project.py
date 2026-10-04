from .database import SessionLocal
from .models import Project


db = SessionLocal()


existing_project = db.query(Project).filter(
    Project.title == "Smart Campus Management"
).first()


if existing_project:

    print("Smart Campus Management already exists.")


else:

    new_project = Project(

        title="Smart Campus Management",

        description="Build a web platform for managing campus activities, events, student services and academic information.",

        skills="html-css,javascript,react,sql",

        category="Web Development"

    )

    db.add(new_project)

    db.commit()

    db.refresh(new_project)

    print(
        "Smart Campus Management added successfully!"
    )

    print(
        "Project ID:",
        new_project.id
    )


db.close()