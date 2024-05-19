function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function animateText(element, text, delay) {
    setTimeout(function() {
        element.textContent = '...';
        setTimeout(function() {
            element.textContent = '';
            let index = 0;
            const interval = setInterval(function() {
                if (index < text.length) {
                    element.textContent += text[index];
                    index++;
                } else {
                    clearInterval(interval);
                }
            }, 50);
        }, 50);
    }, delay);
}
document.addEventListener('DOMContentLoaded', function() {
    const titles = document.querySelectorAll('#dept_name');

    titles.forEach(title => {
        const text = title.textContent;
        title.textContent = '';
        let index = 0;

        function animateText() {
            if (index < text.length) {
                title.textContent += text[index];
                index++;
                setTimeout(animateText, 50);
            }
        }

        animateText();
    });
});

function initiateCall(phoneNumber) {
    window.location.href = "tel:" + phoneNumber;
}
let activeContent = null;

function toggleAccordion(id) {
    const element = document.getElementById(id);
    if (element.style.display === 'block') {
        element.style.display = 'none';
        document.querySelector(`h2[onclick="toggleAccordion('${id}')"]`).classList.remove('active');
        return;
    }
    const contents = document.querySelectorAll('.content');
    contents.forEach(content => {
        content.style.display = 'none';
    });
    if (activeContent) {
        activeContent.classList.remove('active');
    }
    element.style.display = 'block';
    document.querySelector(`h2[onclick="toggleAccordion('${id}')"]`).classList.add('active');
    activeContent = element;
}
window.onclick = function(event) {
    if (!event.target.closest('.accordion')) {
        const contents = document.querySelectorAll('.content');
        contents.forEach(content => {
            content.style.display = 'none';
        });
        const activeTitles = document.querySelectorAll('.active');
        activeTitles.forEach(title => {
            title.classList.remove('active');
        });
    }
}
function loadContent(contentId) {
    let contentSections = document.getElementsByClassName('content-section');
    for (let section of contentSections) {
        section.style.display = 'none';
    }
    let navButtons = document.getElementsByTagName('th');
    for (let button of navButtons) {
        button.classList.remove('active');
    }
    document.getElementById(contentId).style.display = 'block';
    document.getElementById(contentId + '_btn').classList.add('active');
}
window.onload = function() {
    loadContent('vision_mission');
};
document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const facultyName = urlParams.get('faculty');

    const facultyDetails = {
        "Dr.P.Satheesh": {
            "img":"https://mvgrce.com/facultymanager/uploads/files/1pfd9aonui_jch4.jpg",
            "name": "Dr.P.Satheesh",
            "qualification":"M.Tech, Ph.D",
            "designation": "HOD",
            "department":"DATA ENGINEERING",
            "email": "SATISH@MVGRCE.EDU.IN",
            "e":"https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=CllgCJvpbDSHpqFQLqKgXsJGsHDbHSkXhvPLBRcFvLrTWMGTGMnGBwrhtDKVZpghQTDlTvQgrnV",
            "linkedin": "https://www.linkedin.com/in/dr-satheesh/",
            "phone": "+91 XXXXXXXXXX",
            "education": "Masters from Andhra University, Computer Science and Technology specialization",
            "research": "Actively engaged in research in Bioinformatics for which Acharya Nagarjuna University awarded Doctoral Degree",
            "guidance": "Guiding research/projects in the areas of Computational Intelligence. 2 PhDs completed and 3 more ongoing under my guidance",
            "consultancy": "Providing consultancy services to IBCB, Vizag and Bioaxis, Hyderabad",
            "curriculum": "Actively engaged in curriculum design/development for the subjects Software Engineering, and UM",
            "memberships": "Member of Professional bodies like MCSI, MIEEE, MIE, MIAENG, MIAEME, MIBCB",
            "admin": "Apart from academics, contributing with admin responsibility as Convener College ERP, Section Head and Disciplinary member for CSE Department",
            "currentRole": "Currently working as Chair for Computer Society at IEEE Vizag Bay Section",
            "awards": [
                "Won Young researcher award in recognition of contributions to research activities from JNTU Kakinada",
                "Won outstanding scientist award for the contribution and achievement in the field of bioinformatics from Venus international foundation"
            ],
            "experience": "Has diverse experience in both institution for a period of 20 years",
            "startYear": "Has been working since 2002"
        },
        "Dr. Atchuta Rao Sadu": {
            "img":"https://www.mvgrce.com/sites/default/files/2017-06/Achut.jpg",
            "name": "Dr. Atchuta Rao Sadu",
            "qualification":"M.Sc, Ph.D",
            "designation": "ASSOCIATE PROFESSOR",
            "department":"DATA ENGINEERING",
            "email": "DR.ATCHUT.SADU@GMAIL.COM",
            "e":"https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=CllgCJfrLJzNzWGKWDKdwRqdScPlhqsHWmThkChQfCVrcNZnZLSsxPdPSqJPLkqBJXsbvGblmwL",
            "linkedin": "https://www.linkedin.com/in/dr-satheesh/",
            "phone": "+91 XXXXXXXXXX",
            education: "Masters from Andhra University, with Statistics specialization",
            research: "Actively engaged in research in Statistics Models for which Andhra University awarded Doctoral Degree",
            curriculum: "Curriculum design/development for the subjects Quantitative Technology for Managers and Probability Statistics",
            memberships: "Member of Professional bodies like Indian Society Probability & Statistics (ISPC)",
            admin: "Convener, Transport",
            awards: ["Andhra University Doctoral Degree in Statistics Models"],
            experience: "Industry/institution experience for a period of 9 years",
            startYear: "Working since 2007"
        },
        "Dr. V. Jyothi": {
            "img":"https://www.mvgrce.com/sites/default/files/2017-11/Vadisila%20Jyothi.jpg",
            "name": "Dr. V. Jyothi",
            "qualification":"M.Tech, Ph.D",
            "designation": "ASSOCIATE PROFESSOR",
            "department":"DATA ENGINEERING",
            "email": "JYOTHI.VADISALA@GMAIL.COM",
            "e":"https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=CllgCJfrLJzNzWGKWDKdwRqdScPlhqsHWmThkChQfCVrcNZnZLSsxPdPSqJPLkqBJXsbvGblmwL",
            "linkedin": "https://www.linkedin.com/in/dr-satheesh/",
            "phone": "+91 XXXXXXXXXX",
            education: "Masters from Andhra University, with CSE specialization",
            research: "Research on Privacy in Social Networks, for which Andhra University has awarded Ph.D. Actively engaged in research in Data Publishing & Social Networks.",
            guidance: "Guiding research in the areas of Image Processing and Social Networks",
            curriculum: "Curriculum design/development for the subjects Web Technologies, Design Patterns, Distributed Databases, Cloud Computing",
            memberships: "Member of Professional bodies like ISTE",
            admin: "Handling the responsibility of Section Head, CSE(AIML)",
            currentRole: "Certified trainer from WIPRO",
            awards: ["Andhra University Ph.D in Privacy in Social Networks"],
            experience: "Diverse experience in both industry/institution for a period of 12 years",
            startYear: "Working since 2006"
        },
        "Mr. Sura Paparao": {
            "img":"https://mvgrce.com/facultymanager/uploads/files/9mql5huka43_vne.jpg",
            "name": "Mr. Sura Paparao",
            "qualification":"M.Tech",
            "designation": "ASSISTANT PROFESSOR",
            "department":"DATA ENGINEERING",
            "email": "SURAPAPARAO@MVGRCE.EDU.IN",
            "e":"https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=CllgCJfrLJzNzWGKWDKdwRqdScPlhqsHWmThkChQfCVrcNZnZLSsxPdPSqJPLkqBJXsbvGblmwL",
            "linkedin": "https://www.linkedin.com/in/dr-satheesh/",
            "phone": "+91 XXXXXXXXXX",
            education1: {
                1:{ year: "2016", degree: "M. Tech (Computer Science and Engineering)", institution: "Sri Sivani College of Engg." },
                2:{ year: "2012", degree: "B. Tech (Computer Science and Engineering)", institution: "Avanthi Institute of Engg. and Tech." }
            },
            experience: {
                1:{ period: "SEP 2023 to Present", position: "Assistant Professor", institution: "MVGRCE" },
                2:{ period: "DEC 2021 - AUG 2023", position: "Assistant Professor", institution: "AITAM College, Tekkali, Srikakulam" },
                3:{ period: "JAN 2019 - MAY 2021", position: "Guest Faculty", institution: "RGUKT (IIIT Nuzvid)" }
            },
            journalPublications: {
                1:{ title: "Generalized Regression Neural Network Implementation and Computational Analysis of a Knuckle Joint", journal: "NEURO QUANTOLOGY (Q3) An Interdisciplinary Journal of Neuroscience and Quantum Physics", year: "Year not specified", issn: "ISSN 1303-5150", indexing: "[Scopus]" },
                2:{ title: "Analyzing the Effectiveness of Convolutions Neural Networks and Recurrent Neural Networks for Recognizing Facial Expression", journal: "IJFANS International Journal of Food and Nutritional Sciences", year: "Nov 2022", issn: "ISSN Print 2319-1775 Online 2320-7876", indexing: "UGC Care listed (Group -1) Journal" },
                3:{ title: "Statistical Analysis of Various Measures in Auditing Practices Using Optimization Techniques", journal: "Science, Technology and Development Journal", year: "JUNE-2020", issn: "ISSN NO: 0950-0707", indexing: "STD JOURNAL" },
                4:{ title: "A Simulation study: Performance Comparison of AODV and DSR", journal: "International Journal of Advanced Research in Science and Engineering", year: "February 2018", issn: "ISSN (O): 2319-8354, ISSN (P): 2319-8346" },
                5:{ title: "Design and Analysis of a NSBFA Algorithm for Mining Poor Quality Images", journal: "JCT Journals", year: "December 2015", issn: "ISSN: 2278-3814" }
            },
            conferencePapers: {
                1:{ title: "GAN Based Handwritten Digit Recognition System", conference: "2nd International Conference on Cognitive and Intelligent Computing (ICCIC-2022)", location: "Vasavi College of Engineering, Hyderabad", date: "Dec 27-28, 2022", proceedings: "Springer Nature Cognitive Science and Technology series", indexing: "[Scopus]" },
                2:{ title: "VANET based Smart Traffic Monitoring System using Intervention Linear Minimum Spanning Tree (ILMST)", conference: "2nd International Conference on Cognitive and Intelligent Computing (ICCIC-2022)", location: "Vasavi College of Engineering, Hyderabad", date: "Dec 27-28, 2022", proceedings: "Springer Nature Cognitive Science and Technology series", indexing: "[Scopus]" },
                3:{ title: "Chemical Reaction Optimization: A Survey with Application & Challenges in SCDA 2018", conference: "1st International Conference on Soft Computing in Data Analytics (SCDA 2018)", location: "Sri Sivani College of Engineering, Srikakulam, Andhra Pradesh, India", date: "10th – 11th March-2018", proceedings: "Not specified", indexing: "[Scopus]" },
                4:{ title: "WITH CEMENT AS A GEOTECHNICAL CONSTRUCTION MATERIAL", conference: "The 12th International Conference on Recent Innovations in Science, Engineering and Management-2018", location: "Sri Venkateswara College of Engineering & Technology, Etcherla, Srikakulam, Andhra Pradesh", date: "17th February 2018", proceedings: "Not specified", indexing: "Not specified" }
            },
            researchProjects: {
                1:"Chemical Reaction Optimization: A Survey with Application & Challenges in SCDA 2018",
                2:"GAN Based Handwritten Digit Recognition System"
            }, 
            patents:{
                1:{"Indian Patent 202341030816 A":"An Investigation on the usage of Machine Learning Methods for Predicting Employee Performance (Published)"}
            },
            Certifiedcoursescompleted:{
                1:{title:"Completed 8 Weeks of NPTEL-AICTE (Funded by the MoE, Govt of India) Online Certification of Introduction to Research with a Consolidated score of 55%."},
                2:{title:"Completed 12 Weeks of NPTEL-AICTE (Funded by the MoE, Govt of India) Online Certification of Software Testing with a Consolidated score of 52%."},
                3:{title:"Completed 4 Weeks of NPTEL-AICTE (Funded by the MoE, Govt of India) Online Certification of Outcome Based Pedagogic Principles for Effective Teaching with a Consolidated score of 60%."}
            },
            Achievements:{
                1:{title:"Qualified Andhra Pradesh State Eligibility Test (APSET – 2021) for Assistant Professor / Lectureship held on 31st October 2021."},
                2:{title:"Qualified Andhra Pradesh State Eligibility Test (APSET – 2019) for Assistant   Professor / Lectureship held on 20th October 2019."}

            }
        },
        "Dr. P. Srinivasa Rao": {
            "img":"https://mvgrce.com/facultymanager/uploads/files/usqm0ytj14cgheb.jpg",
            "name": "Dr. P. Srinivasa Rao",
            "designation": "ASSOCIATE PROFESSOR",
            "qualification":"Ph.D",
            "department":"DATA ENGINEERING",
            "email": "PSR.CSE@MVGRCE.EDU.IN",
            "e":"https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=CllgCJfrLJzNzWGKWDKdwRqdScPlhqsHWmThkChQfCVrcNZnZLSsxPdPSqJPLkqBJXsbvGblmwL",
            "linkedin": "https://www.linkedin.com/in/dr-satheesh/",
            "phone": "+91 XXXXXXXXXX",
            education: "Masters from JNTUH University, with CSE specialization",
            research: "Actively engaged in research in Machine Learning, Bigdata, AI and Data mining for which JNTUK University awarded Doctoral Degree",
            guidance: "Guiding research/projects in the areas of Machine Learning, Bigdata, AI and Data mining",
            consultancy: "Certified trainer for Big data from NASSCOM organization",
            curriculum: "Curriculum design/development for the subjects Machine Learning, Bigdata, AI and Data mining",
            memberships: "Member of Professional bodies like SMIEE, SMACM, IE, CSI etc.",
            admin: "Contributing with admin responsibility as In-charge Examinations",
            awards: ["JNTUK University Doctoral Degree in Machine Learning, Bigdata, AI and Data mining"],
            experience: "Diverse experience in both industry/institution for a period of 17 years",
            startYear: "Working since 31-10-2011",
            urls: {
                orcid: "https://orcid.org/0000-0003-4851-744X",
                scopus: "https://www.scopus.com/authid/detail.uri?authorId=57195537428",
                publons: "https://publons.com/researcher/2053187/dr-p-srinivasa-rao/",
                researchgate: "https://www.researchgate.net/profile/Srinivas_Rao48"
            }       
        },
        "Sushma Rani N": {
            "img":"https://mvgrce.com/facultymanager/uploads/files/wkdmt8z5uj63y_p.jpg",
            "name": "Sushma Rani N",
            "qualification":"M.Tech (PhD)",
            "designation": "SR. ASSISTANT PROFESSOR",
            "department":"DATA ENGINEERING",
            "email": "SUSHMARANIN@MVGRCE.EDU.IN",
            "e":"https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=CllgCJfrLJzNzWGKWDKdwRqdScPlhqsHWmThkChQfCVrcNZnZLSsxPdPSqJPLkqBJXsbvGblmwL",
            "linkedin": "https://www.linkedin.com/in/dr-satheesh/",
            "phone": "+91 XXXXXXXXXX",
            education: "Masters from JNTUK University, with Computer Science and Engineering specialization",
            research: "Actively engaged in research in Social Network Analysis/ Knowledge Graph Embedding for which NIT, Andhra Pradesh (Pursuing)",
            guidance: "Guiding research/projects in the areas of MACHINE LEARNING, SOCIAL NETWORK ANALYSIS and DATA MINING",
            curriculum: "Curriculum design/development for the subjects Data Structures (A2), Data ware housing and data mining(A1), Data Science and Analytics (A1)",
            memberships: "Member of Professional bodies like IAENG, IEI, INSC",
            admin: "Handling the admin responsibility of Coordinator, CSE(AI&ML). Contributing with admin responsibility as Quality Assurance Cell (Department Level)",
            awards: ["Research Excellence Award- Institute of Scholars, 2019"],
            experience: "Diverse experience in both industry/institution for a period of 15 years",
            startYear: "Has been working since 2011 in MVGRCE",
            patents: "2 Patents Filed and Published",
            publications: "1 Book Published",
        },
        "G.Satya Narayana Reddy": {
            "img":"https://www.mvgrce.com/sites/default/files/2017-01/satyanarayana.jpg",
            "name": "G.Satya Narayana Reddy",
            "qualification":"M.Tech",
            "designation": "DISTINGUISHED ASSISTANT PROFESSOR",
            "department":"DATA ENGINEERING",
            "email": "SATYANARAYANAREDDY@MVGRCE.EDU.IN",
            "e":"https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=CllgCJfrLJzNzWGKWDKdwRqdScPlhqsHWmThkChQfCVrcNZnZLSsxPdPSqJPLkqBJXsbvGblmwL",
            "linkedin": "https://www.linkedin.com/in/dr-satheesh/",
            "phone": "+91 XXXXXXXXXX",
            education: "Masters from Andhra University, with CSIT specialization",
            research: "Guiding research/projects in the areas of System Programming, Cloud Computing, and Block Chain technologies",
            curriculum: "Curriculum design/development for the subjects Computer Programming, Unix & Shell Programming, Network Programming, Operating Systems, and Computer Networks and Salesforce",
            memberships: "Member of Professional bodies like CSIT, ISTE",
            admin: "Contributing with admin responsibility as Coordinator, IoT, Cyber Security with Block Chain",
            currentRole: "Leading Vizag Salesforce Developer Community",
            awards: ["Certified by NPTEL in Block Chain Technologies"],
            experience: "Diverse experience in Institution for a period of 15 years",
            startYear: "Has been working since 2007",
        },
        "Mr. Vella Manikanta": {
            "img":"https://mvgrce.com/facultymanager/uploads/files/gp_lfja680uis7e.jpg",
            "name": "Mr. Vella Manikanta",
            "qualification":"M.Tech, Ph.D",
            "designation": "ASSISTANT PROFESSOR",
            "department":"DATA ENGINEERING",
            "email": "MANIKANTAVELLA48@MVGRCE.EDU.IN",
            "e":"https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=CllgCJfrLJzNzWGKWDKdwRqdScPlhqsHWmThkChQfCVrcNZnZLSsxPdPSqJPLkqBJXsbvGblmwL",
            "linkedin": "https://www.linkedin.com/in/dr-satheesh/",
            "phone": "+91 XXXXXXXXXX",
            education1: {
                1:{ year: "2017", degree: "M. Tech (CSE)", institution: "JNTUK" },
                2:{ year: "2014", degree: "B. Tech (INFORMATION TECHNOLOGY)", institution: "Lendi Institute of Engg. & Tech." }
            },
            experience: {
                1:{ period: "JUL 2023 to Present", position: "Assistant Professor", institution: "MVGRCE" },
                2:{ period: "FEB 2018 - JUN 2023", position: "Assistant Professor", institution: "Raghu Institute of Technology" }
            }
        },
    };

    function generateFacultyDetailsHTML(faculty) {
        let content = '';
        if (faculty.name === "Mr. Sura Paparao") {
            content += `
            <div class="faculty-section">
                    <h2 class="faculty-heading">Education:</h2>
                    ${Object.values(faculty.education1).map(edu => `<p>${edu.year} - ${edu.degree} from ${edu.institution}</p>`).join('')}
                    
                    <h2 class="faculty-heading">Experience:</h2>
                    ${Object.values(faculty.experience).map(exp => `<p>${exp.period} - ${exp.position} at ${exp.institution}</p>`).join('')}
                    
                    <h2 class="faculty-heading">Journal Publications (International/National):</h2>
                    <ol>
                        ${Object.values(faculty.journalPublications).map(pub => `
                            <li>
                                <strong>${pub.title || pub.year || pub.period || pub.degree || pub.position}</strong><br>
                                ${pub.journal || pub.institution || pub.degree || pub.position || pub.conference}<br>
                                ${pub.year || pub.issn || pub.date || pub.location}<br>
                                ${pub.issn || pub.indexing || pub.proceedings || pub.period || pub.position}
                            </li>
                        `).join('')}
                    </ol>
                    
                    <h2 class="faculty-heading">Conference papers (International/National):</h2>
                    <ol>
                        ${Object.values(faculty.conferencePapers).map(paper => `
                            <li>
                                <strong>${paper.title || paper.year || paper.period || paper.degree || paper.position}</strong><br>
                                ${paper.conference || paper.institution || paper.degree || paper.position}<br>
                                ${paper.location || paper.date || paper.proceedings}<br>
                                ${paper.indexing}
                            </li>
                        `).join('')}
                    </ol>
                    
                    <h2 class="faculty-heading">Research Projects:</h2>
                    ${Object.values(faculty.researchProjects).map(project => `<li>${project}</li>`).join('')}

                    <h2 class="faculty-heading">Patents:</h2>
                    <ol>
                        ${Object.values(faculty.patents).map(patent => `
                            <li>${Object.keys(patent)[0]} - ${Object.values(patent)[0]}</li>
                        `).join('')}
                    </ol>
                    
                    <h2 class="faculty-heading">Certified Courses Completed:</h2>
                    <ol>
                        ${Object.values(faculty.Certifiedcoursescompleted).map(course => `
                            <li>${course.title}</li>
                        `).join('')}
                    </ol>
                    
                    <h2 class="faculty-heading">Achievements:</h2>
                    <ol>
                        ${Object.values(faculty.Achievements).map(achievement => `
                            <li>${achievement.title}</li>
                        `).join('')}
                    </ol>
                </div>
            `;
        } else if (faculty.name === "Mr. Vella Manikanta") {
            content = `
                <h2>Education:</h2><br>
                ${Object.values(faculty.education1).map(edu => `${edu.year} - ${edu.degree} from ${edu.institution}`).join('<br>')}<br><br>
                <h2>Experience:</h2><br>
                ${Object.values(faculty.experience).map(exp => `${exp.period} - ${exp.position} at ${exp.institution}`).join('<br>')}<br>`;
        } else {
            let urlsContent = '';
            if (faculty.urls) {
                urlsContent = `
                    <li><strong>Urls:</strong>
                        <ul>
                            ${Object.entries(faculty.urls).map(([key, value]) => `<li><a href="${value}" target="_blank">${key}</a></li>`).join('')}
                        </ul>
                    </li>`;
            }
            let consultancyContent='';
            if(faculty.consultancy){
                consultancyContent=`
                    <li><strong>Consultancy:</strong> ${faculty.consultancy}</li>`;
            }
            let guidancecontent='';
            if(faculty.guidance){
                guidancecontent=`<li><strong>Guidance:</strong> ${faculty.guidance}</li>`;
            }
            content = `
                <ul>
                    <li><strong>Education:</strong> ${faculty.education}</li>
                    <li><strong>Research:</strong> ${faculty.research}</li>
                    ${guidancecontent}
                    ${consultancyContent}
                    <li><strong>Curriculum:</strong> ${faculty.curriculum}</li>
                    <li><strong>Memberships:</strong> ${faculty.memberships}</li>
                    <li><strong>Admin:</strong> ${faculty.admin}</li>
                    <li>${faculty.currentRole}</li>
                    <li><strong>Awards:</strong>
                        <ul>
                            ${faculty.awards.map(award => `<li>${award}</li>`).join('')}
                        </ul>
                    </li>
                    <li><strong>Experience:</strong> ${faculty.experience}</li>
                    <li><strong>Start Year:</strong> ${faculty.startYear}</li>
                    ${urlsContent}
                </ul>
            `;
        }
        return content;
    }

    function getFacultyDetails() {
        const faculty = facultyDetails[facultyName];

        if (faculty) {
            document.getElementById('member_img').src = faculty.img;
            document.getElementById('member_name').textContent = faculty.name;
            document.getElementById('member_qualificaation').textContent = faculty.qualification;
            document.getElementById('member_designation').textContent = faculty.designation;
            document.getElementById('member_department').textContent = faculty.department;
            document.getElementById('member_email').innerHTML = `<a href="${faculty.e}" target="_blank">${faculty.email}</a>`;
            const contactDiv = document.getElementById('member_contact');
            contactDiv.innerHTML = `
                <a href="${faculty.e}" target="_blank">
                    <img src="images/mail.webp" alt="email">
                </a>
                <a href="${faculty.linkedin}" target="_blank">
                    <img src="images/linkedin.webp" alt="linkedin">
                </a>
                <a href="#" onclick="initiateCall('${faculty.phone}')">
                    <img src="images/call.png" alt="call">
                </a>
            `;
            const facultyInfo = document.getElementById('faculty-info');
            facultyInfo.innerHTML = generateFacultyDetailsHTML(faculty);
        } else {
            const facultyContainer = document.getElementById('faculty-container');
            facultyContainer.innerHTML = '<h2>Faculty not found</h2>';
        }
    }

    getFacultyDetails();
});

