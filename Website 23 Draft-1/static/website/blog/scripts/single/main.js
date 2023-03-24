const initialization= (article)=> {
	const content= document.getElementById('content');

	for (let part of article["parts"]) {
		const container= document.createElement('div');
		container.classList.add('article-part-container');

		const header= document.createElement('div');
		header.classList.add('header');

		const title= document.createElement('h3');
		title.innerHTML= part["title"];
		header.appendChild(title);

		if (part["attachedUrl"]) {
			const action= document.createElement('a');
			action.classList.add('main-button');
			action.innerHTML= "See More";
			action.setAttribute('href', part["attachedUrl"]);
			header.appendChild(action);
		}
		
		container.appendChild(header);

		if (part["attachedAsset"]) {
			const asset= document.createElement('div')
			asset.classList.add('asset');
			asset.style.background= `url(/images/assets/${part["attachedAsset"]})`;
			container.appendChild(asset);
		}

		const paragraph= document.createElement('p');
		paragraph.innerHTML= `&nbsp&nbsp&nbsp<span>${part["desc"].substring(0, 1).toUpperCase()}</span>${part["desc"].substring(1)}`;
		container.appendChild(paragraph);

		content.appendChild(container);
	}
}
