let currentActiveMilestone, currentActivePart;

const initialization= (projectData)=> {
	initializeSidePanel(projectData);
}

const initializeSidePanel= (projectData)=> {
	// Header
	document.getElementById('project-name').innerHTML= projectData['title'];
	document.getElementById('project-name').innerTEXT= projectData['title'];
	document.getElementById('project-name').innerText= projectData['title'];

	document.getElementById('client-logo').style.background= `url(http://127.0.0.1:4000/projects/covers/${projectData['id']})`


	const milestonesSection= document.getElementById('milestones');
	milestonesSection.innerHTML= "";
	const legend= document.createElement('legend');
	legend.innerHTML= "Milestones";
	milestonesSection.appendChild(legend);

	for (let milestone_ of projectData["milestones"]) {
		const milestone= document.createElement('button');
		milestone.setAttribute('id', `milestone-${projectData["milestones"].indexOf(milestone_)}`);
		milestone.innerHTML= milestone_["title"].length > 50 ? `${milestone_["title"].subString(0, 50)}...` : milestone_["title"]
		milestone.onclick= ()=> {
			if (currentActiveMilestone == projectData["milestones"].indexOf(milestone_)) {
				return
			}

			if(currentActiveMilestone !== undefined) {
				document.getElementById(`milestone-${currentActiveMilestone}`).classList.remove('active');
			}

			currentActiveMilestone= projectData["milestones"].indexOf(milestone_);
			milestone.classList.add('active');
			displayMilestoneInBodySection(milestone_);
		}
		milestonesSection.appendChild(milestone);

		if (projectData["milestones"].indexOf(milestone_) === 0) {
			currentActiveMilestone= 0;
			milestone.classList.add('active');
			displayMilestoneInBodySection(milestone_);

		}
	}
}


const displayMilestoneInBodySection= (milestone)=> {
	document.getElementById('body-title').innerHTML= milestone["title"];
	document.getElementById('body-desc').innerHTML= milestone["desc"];

	const partsCardsSection= document.querySelector('div#parts > div#cards');
	partsCardsSection.innerHTML= "";

	initializeOverviewCards(milestone);

	for (let partData of milestone["parts"]) {
		const partCard= document.createElement('div');
		partCard.classList.add('part-card')

		const partCardTitle= document.createElement('h4');
		partCardTitle.innerHTML= partData["title"];

		const partCardDesc= document.createElement('p');
		partCardDesc.innerHTML= partData["desc"];

		const categoryLabelCard= document.createElement('div');
		categoryLabelCard.classList.add('label-card');
		categoryLabelCard.innerHTML= partData["category"];
		if (partData["category"] === "Programming") {
			categoryLabelCard.classList.add('blue');
		} else {
			categoryLabelCard.classList.add('yellow');
		}

		const statusLabelCard= document.createElement('div');
		statusLabelCard.classList.add('label-card');
		switch (partData["status"]) {
			case -2:
				statusLabelCard.innerHTML= "Hold";
				statusLabelCard.classList.add('yellow');
				break;
			case -1:
				statusLabelCard.innerHTML= "Not Started";
				statusLabelCard.classList.add('red');
				break;
			case 0:
				statusLabelCard.innerHTML= "In Progress";
				statusLabelCard.classList.add('blue');
				break;
			case 1:
				statusLabelCard.innerHTML= "Done";
				statusLabelCard.classList.add('green');
				break;
			case -2:
				statusLabelCard.innerHTML= "Hold";
				statusLabelCard.classList.add('yellow');
				break;
			case -1:
				statusLabelCard.innerHTML= "Not Started";
				statusLabelCard.classList.add('red');
				break;
		}
		const labels= document.createElement('div');
		labels.setAttribute('id', 'labels');
		labels.appendChild(categoryLabelCard);
		labels.appendChild(statusLabelCard);

		partCard.appendChild(partCardTitle);
		partCard.appendChild(partCardDesc);
		partCard.appendChild(labels);

		partCard.onclick= ()=> {
			if(currentActivePart == milestone["parts"].indexOf(partData)) {
				return;
			}
			currentActivePart= milestone["parts"].indexOf(partData);
			displayPartInInformationSection(milestone['title'], partData);
			toggleLogToResults();
		}
		partsCardsSection.appendChild(partCard);
	}

}

const initializeOverviewCards= (milestoneData)=> {
	const cards= document.querySelector('div#overview > #cards');
	cards.innerHTML= '';

	// Completed Parts Card
	const completedPartsCard= document.createElement('div');
	completedPartsCard.classList.add('overview-card');
	const completedPartsCardTitle= document.createElement('h4');
	completedPartsCardTitle.innerHTML= `<span>${milestoneData["parts"].filter((e)=> e["status"] == 1).length}</span>/${milestoneData['parts'].length} Parts Done`;
	const completedPartsCardBrief= document.createElement('p');
	completedPartsCardBrief.innerHTML= `In this part you will find the count of the done and undone parts of ${milestoneData["title"]}`
	completedPartsCard.appendChild(completedPartsCardTitle);
	completedPartsCard.appendChild(completedPartsCardBrief);
	cards.appendChild(completedPartsCard);

	// Days until End
	const daysUntilEndCard= document.createElement('div');
	daysUntilEndCard.classList.add('overview-card');
	const daysUntilEndCardTitle= document.createElement('h4');
	const startDate= new Date(milestoneData['startDate']);
	const expectedEndDate= new Date(milestoneData['expectedEndDate']);
	daysUntilEndCardTitle.innerHTML= `<span>${Number.parseInt((new Date().getTime()-startDate.getTime())/(1000*3600*24))}</span>/${(expectedEndDate.getTime()-startDate.getTime())/(1000*3600*24)} Days`;
	const daysUntilEndCardBrief= document.createElement('p');
	daysUntilEndCardBrief.innerHTML= `In this part you will find the count of days until ${milestoneData['title']} is done`
	daysUntilEndCard.appendChild(daysUntilEndCardTitle);
	daysUntilEndCard.appendChild(daysUntilEndCardBrief);
	cards.appendChild(daysUntilEndCard);
	
	// Results Blog Sections Available
	let resultSectionsCount= 0;
	milestoneData['parts'].map(e => resultSectionsCount += e['results'].length);
	const resultsBlogSectionsCard= document.createElement('div');
	resultsBlogSectionsCard.classList.add('overview-card');
	const resultsBlogSectionsCardTitle= document.createElement('h4');
	resultsBlogSectionsCardTitle.innerHTML= `<span>${resultSectionsCount}</span> Result Sections`
	const resultsBlogSectionsCardBrief= document.createElement('p');
	resultsBlogSectionsCardBrief.innerHTML= `In this part you will find the count of published results' blog sections`
	resultsBlogSectionsCard.appendChild(resultsBlogSectionsCardTitle);
	resultsBlogSectionsCard.appendChild(resultsBlogSectionsCardBrief);
	cards.appendChild(resultsBlogSectionsCard);

	// Log Sections Available
	let logSectionsCount= 0;
	milestoneData['parts'].map(e => logSectionsCount += e['log'].length);
	const logSectionsPartsCard= document.createElement('div');
	logSectionsPartsCard.classList.add('overview-card');
	const logSectionsPartsCardTitle= document.createElement('h4');
	logSectionsPartsCardTitle.innerHTML= `<span>${logSectionsCount}</span> Log Sections`
	const logSectionsPartsCardBrief= document.createElement('p');
	logSectionsPartsCardBrief.innerHTML= `In this part you will find the count of published log' blog sections`
	logSectionsPartsCard.appendChild(logSectionsPartsCardTitle);
	logSectionsPartsCard.appendChild(logSectionsPartsCardBrief);
	cards.appendChild(logSectionsPartsCard);
}

const displayPartInInformationSection= (milestoneTitle, partData)=> {
	document.getElementById('information-panel-placeholder').style.display="none";
	document.getElementById('information-panel').style.display="flex";
	document.getElementById('information-panel-title').innerHTML= `<span>${milestoneTitle}</span><br>${partData['title']}`;
	document.getElementById('information-panel-desc').innerHTML= `${partData['desc']}`;

	for (let logPart of partData['log']) {
		const logPartCard= document.createElement('div');
		logPartCard.classList.add('log-card')
		const logPartCardTitle= document.createElement('h5');
		logPartCardTitle.innerHTML= `<span>${logPart['publishedIn']}</span><br>>${logPart['title']}`;

		const logPartCardBrief= document.createElement('p')
		logPartCardBrief.innerHTML= logPart['desc'];

		logPartCard.appendChild(logPartCardTitle);
		logPartCard.appendChild(logPartCardBrief);

		document.getElementById('log-fragment').appendChild(logPartCard);
	}

	for (let resultPart of partData['results']) {
		const resultPartCard= document.createElement('div');
		resultPartCard.classList.add('result-blog-section')

		const resultPartCardTitle= document.createElement('h5');
		resultPartCardTitle.innerHTML= `<span>${resultPart['publishedIn']}</span><br>>${resultPart['title']}`;

		const resultPartCardBrief= document.createElement('p')
		resultPartCardBrief.innerHTML= resultPart['desc'];

		resultPartCard.appendChild(resultPartCardTitle);
		if(resultPart['asset'] != undefined) {
			const asset= document.createElement('div');
			asset.setAttribute('id', 'asset');
			asset.style.backgroundImage= `url(http://127.0.0.1:4000/projects/assets/${resultPart['asset']}`;
			resultPartCard.appendChild(asset);
		}

		resultPartCard.appendChild(resultPartCardBrief);

		document.getElementById('result-fragment').appendChild(resultPartCard);
	}
}

const toggleResultsToLog= ()=> {
	const logController= document.getElementById('log-controller');
	const resultsController= document.getElementById('results-controller');

	const logFragment= document.getElementById('log-fragment');
	const resultsFragment= document.getElementById('result-fragment');

	if (resultsFragment.style.display === "flex") {
		return;
	}

	logFragment.style.display= "none";
	logController.classList.remove('active-fragment-controller');
	resultsFragment.style.display= "flex";
	resultsController.classList.add('active-fragment-controller');


}

const toggleLogToResults= ()=> {
	const logController= document.getElementById('log-controller');
	const resultsController= document.getElementById('results-controller');

	const logFragment= document.getElementById('log-fragment');
	const resultsFragment= document.getElementById('result-fragment');

	if (logFragment.style.display === "flex") {
		return;
	}

	resultsFragment.style.display= "none";
	resultsController.classList.remove('active-fragment-controller');
	logFragment.style.display= "flex";
	logController.classList.add('active-fragment-controller');
}