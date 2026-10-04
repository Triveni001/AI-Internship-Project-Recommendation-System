function saveSkills() {

    const selectedSkills = [];

    const checkboxes = document.querySelectorAll(
        'input[name="skill"]:checked'
    );

    if (checkboxes.length === 0) {
        alert("Please select at least one skill.");
        return;
    }

    checkboxes.forEach(function (checkbox) {
        selectedSkills.push(checkbox.value);
    });

    localStorage.setItem(
        "studentSkills",
        JSON.stringify(selectedSkills)
    );

    window.location.href = "interests.html";
}


function saveInterests() {

    const selectedInterests = [];

    const checkboxes = document.querySelectorAll(
        'input[name="interest"]:checked'
    );

    if (checkboxes.length === 0) {
        alert("Please select at least one interest.");
        return;
    }

    checkboxes.forEach(function (checkbox) {
        selectedInterests.push(checkbox.value);
    });

    localStorage.setItem(
        "studentInterests",
        JSON.stringify(selectedInterests)
    );

    window.location.href = "dashboard.html";
}


function calculateMatch(studentSkills, requiredSkills) {

    let matchedSkills = 0;

    requiredSkills.forEach(function (skill) {

        if (studentSkills.includes(skill)) {
            matchedSkills++;
        }

    });

    const percentage =
        (matchedSkills / requiredSkills.length) * 100;

    return Math.round(percentage);
}


function showRecommendations() {

    const savedSkills =
        JSON.parse(localStorage.getItem("studentSkills")) || [];

    const savedInterests =
        JSON.parse(localStorage.getItem("studentInterests")) || [];


    // Python Developer Internship

    let match1 = calculateMatch(
        savedSkills,
        ["python", "sql", "git"]
    );

    if (
        savedInterests.includes("software") ||
        savedInterests.includes("data")
    ) {
        match1 = Math.min(match1 + 10, 100);
    }


    // Machine Learning Internship

    let match2 = calculateMatch(
        savedSkills,
        ["python", "machine-learning", "data-science"]
    );

    if (
        savedInterests.includes("ai") ||
        savedInterests.includes("ml") ||
        savedInterests.includes("data")
    ) {
        match2 = Math.min(match2 + 10, 100);
    }


    // Frontend Developer Internship

    let match3 = calculateMatch(
        savedSkills,
        ["html-css", "javascript", "react"]
    );

    if (
        savedInterests.includes("web") ||
        savedInterests.includes("software")
    ) {
        match3 = Math.min(match3 + 10, 100);
    }


    const matchElement1 =
        document.getElementById("match1");

    const matchElement2 =
        document.getElementById("match2");

    const matchElement3 =
        document.getElementById("match3");


    if (matchElement1) {
        matchElement1.innerText =
            "Match: " + match1 + "%";
    }


    if (matchElement2) {
        matchElement2.innerText =
            "Match: " + match2 + "%";
    }


    if (matchElement3) {
        matchElement3.innerText =
            "Match: " + match3 + "%";
    }
}


if (document.getElementById("match1")) {
    showRecommendations();
}
function applyInternship(internshipName, companyName) {

    localStorage.setItem(
        "appliedInternship",
        internshipName
    );

    localStorage.setItem(
        "appliedCompany",
        companyName
    );

    localStorage.setItem(
        "applicationStatus",
        "Applied"
    );

    alert("Application submitted successfully!");

    window.location.href = "applications.html";
}
function showApplication() {

    const internship =
        localStorage.getItem("appliedInternship");

    const company =
        localStorage.getItem("appliedCompany");

    const status =
        localStorage.getItem("applicationStatus");

    const nameElement =
        document.getElementById("applicationName");

    const companyElement =
        document.getElementById("companyName");

    const statusElement =
        document.getElementById("applicationStatus");


    if (nameElement && internship) {
        nameElement.innerText = internship;
    }

    if (companyElement && company) {
        companyElement.innerText = company;
    }

    if (statusElement && status) {
        statusElement.innerText =
            "Application Status: " + status;
    }
}


if (document.getElementById("applicationName")) {
    showApplication();
}
function registerUser() {

    const name = document.querySelector(
        'input[name="fullName"]'
    ).value;

    const email = document.querySelector(
        'input[name="email"]'
    ).value;

    const password = document.querySelector(
        'input[name="password"]'
    ).value;

    const branch = document.querySelector(
        'select[name="branch"]'
    ).value;


    if (
        name === "" ||
        email === "" ||
        password === "" ||
        branch === ""
    ) {
        alert("Please fill all registration details.");
        return;
    }


    localStorage.setItem("studentName", name);

    localStorage.setItem("studentEmail", email);

    localStorage.setItem("studentPassword", password);

    localStorage.setItem("studentBranch", branch);


    alert("Registration successful!");

    window.location.href = "login.html";
}

function loginUser() {

    const email = document.querySelector(
        'input[type="email"]'
    ).value;

    const password = document.querySelector(
        'input[type="password"]'
    ).value;


    const savedEmail =
        localStorage.getItem("studentEmail");

    const savedPassword =
        localStorage.getItem("studentPassword");


    if (email === "" || password === "") {
        alert("Please enter email and password.");
        return;
    }


    if (
        email === savedEmail &&
        password === savedPassword
    ) {

        localStorage.setItem(
            "loggedIn",
            "true"
        );

        alert("Login successful!");

        window.location.href = "profile.html";

    } else {

        alert("Invalid email or password.");

    }
}
function saveProfile() {

    const college =
        document.querySelector(
            'input[name="college"]'
        ).value;

    const degree =
        document.querySelector(
            'select[name="degree"]'
        ).value;

    const graduationYear =
        document.querySelector(
            'select[name="graduationYear"]'
        ).value;

    const technicalSkills =
        document.querySelector(
            'input[name="technicalSkills"]'
        ).value;

    const interests =
        document.querySelector(
            'input[name="profileInterests"]'
        ).value;

    const projects =
        document.querySelector(
            'input[name="projects"]'
        ).value;

    const certifications =
        document.querySelector(
            'input[name="certifications"]'
        ).value;


    if (
        college === "" ||
        degree === "" ||
        graduationYear === "" ||
        technicalSkills === "" ||
        interests === ""
    ) {

        alert("Please fill all required details.");

        return;
    }


    localStorage.setItem(
        "college",
        college
    );

    localStorage.setItem(
        "degree",
        degree
    );

    localStorage.setItem(
        "graduationYear",
        graduationYear
    );

    localStorage.setItem(
        "technicalSkills",
        technicalSkills
    );

    localStorage.setItem(
        "profileInterests",
        interests
    );

    localStorage.setItem(
        "projects",
        projects
    );

    localStorage.setItem(
        "certifications",
        certifications
    );


    alert("Profile saved successfully!");

    window.location.href = "skills.html";
}
function addProject(projectName) {

    let myProjects =
        JSON.parse(localStorage.getItem("myProjects")) || [];


    if (!myProjects.includes(projectName)) {

        myProjects.push(projectName);

        localStorage.setItem(
            "myProjects",
            JSON.stringify(myProjects)
        );

        alert(
            projectName + " added to My Projects!"
        );

    } else {

        alert(
            projectName + " is already in My Projects."
        );

    }

    window.location.href = "my-projects.html";
}
function showMyProjects() {

    const myProjects =
        JSON.parse(localStorage.getItem("myProjects")) || [];

    const container =
        document.getElementById("myProjectsContainer");


    if (!container) {
        return;
    }


    if (myProjects.length === 0) {
        return;
    }


    container.innerHTML = "";


    myProjects.forEach(function (project) {

        const card =
            document.createElement("div");

        card.className = "internship-card";


        card.innerHTML = `
            <h2>${project}</h2>

            <p>
                This project has been added
                to your project list.
            </p>

            <div class="match">
                Added
            </div>
        `;


        container.appendChild(card);

    });
}


if (
    document.getElementById("myProjectsContainer")
) {
    showMyProjects();
}
function showProfile() {

    function getValue(key) {
        return localStorage.getItem(key) || "Not provided";
    }

    const profileData = {
        profileName: "studentName",
        profileEmail: "studentEmail",
        profileBranch: "studentBranch",
        profileCollege: "college",
        profileDegree: "degree",
        profileYear: "graduationYear",
        profileSkills: "technicalSkills",
        profileInterests: "profileInterests",
        profileProjects: "projects",
        profileCertifications: "certifications"
    };

    Object.keys(profileData).forEach(function(id) {

        const element = document.getElementById(id);

        if (element) {
            element.innerText =
                getValue(profileData[id]);
        }

    });
}

if (document.getElementById("profileName")) {
    showProfile();
}
function showSkillGap() {

    const studentSkills =
        JSON.parse(localStorage.getItem("studentSkills")) || [];

    const pythonStatus =
        document.getElementById("pythonStatus");

    const sqlStatus =
        document.getElementById("sqlStatus");

    const mlStatus =
        document.getElementById("mlStatus");

    const nlpStatus =
        document.getElementById("nlpStatus");


    if (pythonStatus) {

        if (studentSkills.includes("python")) {
            pythonStatus.innerText = "Strong";
        } else {
            pythonStatus.innerText = "Learn";
        }

    }


    if (sqlStatus) {

        if (studentSkills.includes("sql")) {
            sqlStatus.innerText = "Strong";
        } else {
            sqlStatus.innerText = "Needs Practice";
        }

    }


    if (mlStatus) {

        if (studentSkills.includes("machine-learning")) {
            mlStatus.innerText = "Strong";
        } else {
            mlStatus.innerText = "Needs Improvement";
        }

    }


    if (nlpStatus) {

        if (studentSkills.includes("data-science")) {
            nlpStatus.innerText = "Needs Practice";
        } else {
            nlpStatus.innerText = "Learn";
        }

    }

}


if (document.getElementById("pythonStatus")) {
    showSkillGap();
}
async function registerWithBackend() {

    const name =
        document.getElementById("fullName").value;

    const email =
        document.getElementById("email").value;

    const password =
        document.getElementById("password").value;

    const branch =
        document.getElementById("branch").value;


    if (
        name === "" ||
        email === "" ||
        password === "" ||
        branch === ""
    ) {

        alert("Please fill all registration details.");

        return;
    }


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/register",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    name: name,
                    email: email,
                    password: password,
                    branch: branch
                })
            }
        );


        const data = await response.json();


        if (response.ok) {

            alert(
                "Registration successful! Student ID: "
                + data.student_id
            );

            window.location.href = "login.html";

        } else {

            alert(
                "Registration failed: "
                + (data.detail || "Unknown error")
            );

        }

    } catch (error) {

        alert(
            "Backend server connection failed."
        );

        console.error(error);
    }
}
async function loginWithBackend() {

    const email =
        document.getElementById("loginEmail").value;

    const password =
        document.getElementById("loginPassword").value;


    if (email === "" || password === "") {

        alert("Please enter email and password.");

        return;
    }


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/login",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    email: email,
                    password: password
                })
            }
        );


        const data = await response.json();


        if (response.ok) {

            localStorage.setItem(
                "loggedIn",
                "true"
            );

            localStorage.setItem(
                "studentId",
                data.student_id
            );

            localStorage.setItem(
                "studentName",
                data.name
            );

            alert("Login successful!");

            window.location.href =
                "profile.html";

        } else {

            alert(
                data.detail || "Invalid email or password."
            );

        }

    } catch (error) {

        alert(
            "Backend server connection failed."
        );

        console.error(error);
    }
}
async function loadProfileFromBackend() {

    const studentId =
        localStorage.getItem("studentId");

    if (!studentId) {

        alert("Please login first.");

        window.location.href =
            "login.html";

        return;
    }


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/student/"
            + studentId
        );


        const data =
            await response.json();


        if (!response.ok) {

            alert(
                data.detail ||
                "Unable to load profile."
            );

            return;
        }


        document.getElementById(
            "profileName"
        ).innerText = data.name;


        document.getElementById(
            "profileEmail"
        ).innerText = data.email;


        document.getElementById(
            "profileBranch"
        ).innerText =
            data.branch || "Not provided";


        document.getElementById(
            "profileCollege"
        ).innerText =
            data.college || "Not provided";


        document.getElementById(
            "profileDegree"
        ).innerText =
            data.degree || "Not provided";


        document.getElementById(
            "profileYear"
        ).innerText =
            data.graduation_year || "Not provided";


        document.getElementById(
            "profileSkills"
        ).innerText =
            data.technical_skills || "Not provided";


        document.getElementById(
            "profileInterests"
        ).innerText =
            data.interests || "Not provided";


        document.getElementById(
            "profileProjects"
        ).innerText =
            data.projects || "Not provided";


        document.getElementById(
            "profileCertifications"
        ).innerText =
            data.certifications || "Not provided";

    }
    catch (error) {

        alert(
            "Backend server connection failed."
        );

        console.error(error);
    }
}


if (
    document.getElementById("profileName")
) {

    loadProfileFromBackend();

}
async function saveProfileToBackend() {

    const studentId =
        localStorage.getItem("studentId");

    if (!studentId) {
        alert("Please login first.");
        window.location.href = "login.html";
        return;
    }

    const profile = {
        college: document.getElementById("college").value,
        degree: document.getElementById("degree").value,
        graduation_year:
            document.getElementById("graduationYear").value,
        technical_skills:
            document.getElementById("technicalSkills").value,
        interests:
            document.getElementById("profileInterests").value,
        projects:
            document.getElementById("projects").value,
        certifications:
            document.getElementById("certifications").value
    };

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/student/"
            + studentId + "/profile",
            {
                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(profile)
            }
        );

        const data = await response.json();

        if (response.ok) {

            alert("Profile saved to database!");

            window.location.href =
                "skills.html";

        } else {

            alert(
                data.detail || "Profile update failed."
            );
        }

    } catch (error) {

        alert("Backend server connection failed.");

        console.error(error);
    }
}
async function saveSkillsToBackend() {

    const studentId =
        localStorage.getItem("studentId");

    if (!studentId) {

        alert("Please login first.");

        window.location.href = "login.html";

        return;
    }

    const selectedSkills = [];

    const checkboxes =
        document.querySelectorAll(
            'input[name="skill"]:checked'
        );

    if (checkboxes.length === 0) {

        alert("Please select at least one skill.");

        return;
    }

    checkboxes.forEach(function(checkbox) {

        selectedSkills.push(checkbox.value);

    });


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/student/"
            + studentId + "/skills",
            {
                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    skills: selectedSkills.join(",")
                })
            }
        );


        const data = await response.json();


        if (response.ok) {

            localStorage.setItem(
                "studentSkills",
                JSON.stringify(selectedSkills)
            );

            alert("Skills saved to database!");

            window.location.href =
                "interests.html";

        } else {

            alert(
                data.detail || "Unable to save skills."
            );

        }

    } catch (error) {

        alert(
            "Backend server connection failed."
        );

        console.error(error);
    }
}
async function saveInterestsToBackend() {

    const studentId =
        localStorage.getItem("studentId");

    if (!studentId) {

        alert("Please login first.");

        window.location.href = "login.html";

        return;
    }

    const selectedInterests = [];

    const checkboxes =
        document.querySelectorAll(
            'input[name="interest"]:checked'
        );

    if (checkboxes.length === 0) {

        alert("Please select at least one interest.");

        return;
    }

    checkboxes.forEach(function(checkbox) {

        selectedInterests.push(
            checkbox.value
        );

    });


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/student/"
            + studentId + "/interests",
            {
                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    interests:
                        selectedInterests.join(",")
                })
            }
        );


        const data =
            await response.json();


        if (response.ok) {

            localStorage.setItem(
                "studentInterests",
                JSON.stringify(selectedInterests)
            );

            alert(
                "Interests saved to database!"
            );

            window.location.href =
                "dashboard.html";

        } else {

            alert(
                data.detail ||
                "Unable to save interests."
            );
        }

    } catch (error) {

        alert(
            "Backend server connection failed."
        );

        console.error(error);
    }
}
async function loadInternshipsFromBackend() {
    try {
        const response = await fetch("http://127.0.0.1:8000/internships");

        const internships = await response.json();

        console.log("Backend internships:", internships);
    } catch (error) {
        console.error("Backend connection failed:", error);
    }
}
if (document.getElementById("match1")) {
    loadInternshipsFromBackend();
}
async function applyInternshipToBackend(
    internshipId,
    internshipTitle,
    company
) {

    const studentId =
        localStorage.getItem("studentId");

    if (!studentId) {

        alert("Please login first.");

        window.location.href =
            "login.html";

        return;
    }

    try {

        const response = await fetch(
            `http://127.0.0.1:8000/student/${studentId}/apply/${internshipId}`,
            {
                method: "POST"
            }
        );

        const result =
            await response.json();

        if (!response.ok) {

            alert(
                result.detail ||
                "Application failed."
            );

            return;
        }

        alert(
            "Application submitted successfully!"
        );

        window.location.href =
            "applications.html";

    } catch (error) {

        console.error(error);

        alert(
            "Unable to connect to backend."
        );
    }
}