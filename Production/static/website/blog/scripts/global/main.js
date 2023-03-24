let blogData;

const initialization= (blogData_)=> {
	blogData= blogData_;
	if (window.addEventListener) {
		window.addEventListener('load', ()=> { initArticlesSection(undefined) });
	} else if (window.attachEvent) {
		window.attachEvent('onload', ()=> { initArticlesSection(undefined) });
	}
}

const search= ()=> {
	const searchField= document.getElementById('token-field');
	initArticlesSection({
		token: searchField.value.trim(),
	})
}


const initArticlesSection= (searchParams)=> {
	const articlesSection= document.querySelector('section#cards > div#body > div#cards');
	const articlesSectionHeaderTitle= document.querySelector('section#cards > div#body > div#header > h4');
	const articlesSectionHeaderAction= document.querySelector('section#cards > div#body > div#header > button');
	const filterMsg= document.getElementById('filtration-msg');

	articlesSection.innerHTML= "";
	if (searchParams) {
		const articles= blogData.filter(e=> e["title"].toLowerCase().includes(searchParams.token.toLowerCase() || '') || e["id"].includes(searchParams.token));
		if (articles.length === 0) {
			filterMsg.innerHTML= `No Articles Found`;
			return;
		}

		articlesSectionHeaderTitle.innerHTML= `<span>(${articles.length})</span> Articles`

		articlesSectionHeaderAction.style.display= "flex";
		articlesSectionHeaderAction.onclick= ()=> { initArticlesSection(undefined); }

		for (blog of articles){
			articlesSection.appendChild(genereateArticleCard(blog));
		}
		filterMsg.innerHTML= `(${articles.length}) Article/s Found`;
		return;
	}

	filterMsg.innerHTML= "";
	articlesSectionHeaderTitle.innerHTML= `<span>(${blogData.length})</span> Articles`
	articlesSectionHeaderAction.style.display= "none";
	articlesSectionHeaderAction.onclick= ()=> { }
	for (let blog of blogData) {
		articlesSection.appendChild(genereateArticleCard(blog));
	}

}

const genereateArticleCard= (blog)=> {
	const articleCard= document.createElement('div');
	articleCard.onclick= ()=> {
		window.open(`/articles/${blog["id"]}`, '_self')
	}
	articleCard.classList.add('article-card');

	const cover= document.createElement('div');
	cover.classList.add('cover');
	cover.style.backgroundImage= `url(/images/blogCovers/${blog["id"]})`;
	articleCard.appendChild(cover);

	const title= document.createElement('h2');
	title.innerHTML= blog["title"].length >= 75 ? `${blog["title"].substring(0, 75)}...` : blog["title"];
	articleCard.appendChild(title);

	const shortBrief= document.createElement('p');
	shortBrief.innerHTML= blog["shortBrief"];
	articleCard.appendChild(shortBrief);

	const rating= document.createElement('div');
	rating.classList.add('rating');
	
	const ratingInner=document.createElement('div');
	generateRatingBar(ratingInner, blog["overallRating"]);
	rating.appendChild(ratingInner);

	const ratingCount= document.createElement('p');
	ratingCount.innerHTML= `(${blog["reviews"].length})`;
	rating.appendChild(ratingCount);
	
	articleCard.appendChild(rating);

	const actions= document.createElement('div');
	actions.classList.add('actions');
	const mainAction= document.createElement('button');
	mainAction.setAttribute('id', 'action');
	const actionInner= document.createElement('i');
	actionInner.classList.add('fa');
	actionInner.classList.add('fa-arrow-right');
	mainAction.appendChild(actionInner);
	actions.appendChild(mainAction);
	articleCard.appendChild(actions);

	return articleCard;
}

const generateRatingBar= (container, rating)=> {
	const starOne= document.createElement('span');
	starOne.classList.add('fa');
	starOne.classList.add('checked');
	const starTwo= document.createElement('span');
	starTwo.classList.add('fa');
	starTwo.classList.add('checked');
	const starThree= document.createElement('span');
	starThree.classList.add('fa');
	starThree.classList.add('checked');
	const starFour= document.createElement('span');
	starFour.classList.add('fa');
	starFour.classList.add('checked');
	const starFive= document.createElement('span');
	starFive.classList.add('fa');
	starFive.classList.add('checked');

	switch(true) {
		case rating >= 0 && rating < 0.5:
			starOne.classList.add('fa-star-o');
			starTwo.classList.add('fa-star-o');
			starThree.classList.add('fa-star-o');
			starFour.classList.add('fa-star-o');
			starFive.classList.add('fa-star-o');
			break;
		case rating >= 0.5 && rating < 1:
			starOne.classList.add('fa-star-half-o');
			starTwo.classList.add('fa-star-o');
			starThree.classList.add('fa-star-o');
			starFour.classList.add('fa-star-o');
			starFive.classList.add('fa-star-o');
			break;
		case rating >= 1 && rating < 1.5:
			starOne.classList.add('fa-star');
			starTwo.classList.add('fa-star-o');
			starThree.classList.add('fa-star-o');
			starFour.classList.add('fa-star-o');
			starFive.classList.add('fa-star-o');
			break;
		case rating >= 1.5 && rating < 2:
			starOne.classList.add('fa-star');
			starTwo.classList.add('fa-star-half-o');
			starThree.classList.add('fa-star-o');
			starFour.classList.add('fa-star-o');
			starFive.classList.add('fa-star-o');
			break;
		case rating >= 2 && rating < 2.5:
			starOne.classList.add('fa-star');
			starTwo.classList.add('fa-star');
			starThree.classList.add('fa-star-o');
			starFour.classList.add('fa-star-o');
			starFive.classList.add('fa-star-o');
			break;
		case rating >= 2.5 && rating < 3:
			starOne.classList.add('fa-star');
			starTwo.classList.add('fa-star');
			starThree.classList.add('fa-star-half-o');
			starFour.classList.add('fa-star-o');
			starFive.classList.add('fa-star-o');
			break;
		case rating >= 3 && rating < 3.5:
			starOne.classList.add('fa-star');
			starTwo.classList.add('fa-star');
			starThree.classList.add('fa-star');
			starFour.classList.add('fa-star-o');
			starFive.classList.add('fa-star-o');
			break;
		case rating >= 3.5 && rating < 4:
			starOne.classList.add('fa-star');
			starTwo.classList.add('fa-star');
			starThree.classList.add('fa-star');
			starFour.classList.add('fa-star-half-o');
			starFive.classList.add('fa-star-o');
			break;
		case rating >= 4 && rating < 4.5:
			starOne.classList.add('fa-star');
			starTwo.classList.add('fa-star');
			starThree.classList.add('fa-star');
			starFour.classList.add('fa-star');
			starFive.classList.add('fa-star-o');
			break;
		case rating >= 4.5 && rating < 5:
			starOne.classList.add('fa-star');
			starTwo.classList.add('fa-star');
			starThree.classList.add('fa-star');
			starFour.classList.add('fa-star');
			starFive.classList.add('fa-star-half-o');
			break;
		case rating == 5:
			starOne.classList.add('fa-star');
			starTwo.classList.add('fa-star');
			starThree.classList.add('fa-star');
			starFour.classList.add('fa-star');
			starFive.classList.add('fa-star');
			break;
	}

	container.appendChild(starOne);
	container.appendChild(starTwo);
	container.appendChild(starThree);
	container.appendChild(starFour);
	container.appendChild(starFive);
}