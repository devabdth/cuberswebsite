let currentWebsiteSlide, currentApplicationSlide, currentSystemSlide;
const initializeWebsitesCarousel= (lang, slides_)=> {
	let websiteSlides= slides_;
	const fragment= document.querySelector('div.fragment#websites');
	const slides= document.querySelector('div.slides#websites');

	// Creating Slides
	for (let s of slides_) {
		const fragmentSlide= document.createElement('div');
		fragmentSlide.classList.add('fragment-slide');
		fragmentSlide.classList.add('websites');
		fragmentSlide.setAttribute('id', `fragment-slide-${slides_.indexOf(s)}`);
		fragmentSlide.style.backgroundImage= `url(../images/covers/${s["id"]})`
		

		const title= document.createElement('h3');
		title.innerHTML= s["title"];
		title.innerText= s["title"];
		title.innerTEXT= s["title"];

		const paragraph= document.createElement('p');
		paragraph.innerHTML= s["short_brief"];
		paragraph.innerText= s["short_brief"];
		paragraph.innerTEXT= s["short_brief"];

		const action= document.createElement('a');
		action.innerHTML= lang == "en" ? "See More!" : "إقرأ المزيد!"
		action.classList.add('main-button');
		action.setAttribute('href', s["action"]);

		const actionsDiv= document.createElement('div');
		actionsDiv.classList.add('actions');
		actionsDiv.appendChild(action);

		const contentDiv= document.createElement('div');
		contentDiv.classList.add('content');
		contentDiv.appendChild(title);
		contentDiv.appendChild(paragraph);
		contentDiv.appendChild(actionsDiv);

		fragmentSlide.appendChild(contentDiv);
		fragment.appendChild(fragmentSlide)

		fragment.appendChild(fragmentSlide);
	}

	// Creating Slides Controllers
	for (let i= 0; i!= websiteSlides.length; i++) {
		let slide= document.createElement('div');
		slide.classList.add('carousel-slide');
		slide.classList.add('websites');
		slide.setAttribute('id', `slide-${i}`);
		slide.onclick= ()=> {
			pickSlide({
				section: 'websites',
				slide: i,
				totalSlides: websiteSlides.length,
				changeCurrentSlide: (i)=> { currentWebsiteSlide= i; }
			})
		}
		slides.appendChild(slide);

	}
	// Carousel Controllers
	const leftCarouselController= document.querySelector('div.left-carousel-controller#websites');
	leftCarouselController.onclick= ()=> {
		if (currentWebsiteSlide === 0) {
			pickSlide({
				section: 'websites',
				slide: (websiteSlides.length - 1),
				totalSlides: websiteSlides.length,
				changeCurrentSlide: (i)=> { currentWebsiteSlide= i; }
			});
			return;
		}
		pickSlide({
			section: 'websites',
			slide: currentWebsiteSlide - 1,
			totalSlides: websiteSlides.length,
			changeCurrentSlide: (i)=> { currentWebsiteSlide= i; }
		});
	}
	const rightCarouselController= document.querySelector('div.right-carousel-controller#websites');
	rightCarouselController.onclick= ()=> {
		if (currentWebsiteSlide === (websiteSlides.length - 1)) {
			pickSlide({
				section: 'websites',
				slide: 0,
				totalSlides: websiteSlides.length,
				changeCurrentSlide: (i)=> { currentWebsiteSlide= i; }
			});
			return;
		}
		pickSlide({
			section: 'websites',
			slide: currentWebsiteSlide + 1,
			totalSlides: websiteSlides.length,
			changeCurrentSlide: (i)=> { currentWebsiteSlide= i; }
		});
	}
}


const initializeApplicationsCarousel= (lang, slides_)=> {
	let applicationSlides= slides_;
	const fragment= document.querySelector('div.fragment#applications');
	const slides= document.querySelector('div.slides#applications');

	// Creating Slides
	for (let s of slides_) {
		const fragmentSlide= document.createElement('div');
		fragmentSlide.classList.add('fragment-slide');
		fragmentSlide.classList.add('applications');
		fragmentSlide.setAttribute('id', `fragment-slide-${slides_.indexOf(s)}`);
		fragmentSlide.style.backgroundImage= `url(/images/covers/${s["id"]})`
		

		const title= document.createElement('h3');
		title.innerHTML= s["title"];
		title.innerText= s["title"];
		title.innerTEXT= s["title"];

		const paragraph= document.createElement('p');
		paragraph.innerHTML= s["short_brief"];
		paragraph.innerText= s["short_brief"];
		paragraph.innerTEXT= s["short_brief"];

		const action= document.createElement('a');
		action.innerHTML= lang == "en" ? "See More!" : "إقرأ المزيد!"
		action.classList.add('main-button');
		action.setAttribute('href', s["action"]);

		const actionsDiv= document.createElement('div');
		actionsDiv.classList.add('actions');
		actionsDiv.appendChild(action);

		const contentDiv= document.createElement('div');
		contentDiv.classList.add('content');
		contentDiv.appendChild(title);
		contentDiv.appendChild(paragraph);
		contentDiv.appendChild(actionsDiv);

		fragmentSlide.appendChild(contentDiv);
		fragment.appendChild(fragmentSlide)

		fragment.appendChild(fragmentSlide);
	}

	// Creating Slides Controllers
	for (let i= 0; i!= applicationSlides.length; i++) {
		let slide= document.createElement('div');
		slide.classList.add('carousel-slide');
		slide.classList.add('applications');
		slide.setAttribute('id', `slide-${i}`);
		slide.onclick= ()=> {
			pickSlide({
				section: 'applications',
				slide: i,
				totalSlides: applicationSlides.length,
				changeCurrentSlide: (i)=> { currentApplicationSlide= i; }
			})
		}
		slides.appendChild(slide);

	}
	// Carousel Controllers
	const leftCarouselController= document.querySelector('div.left-carousel-controller#applications');
	leftCarouselController.onclick= ()=> {
		if (currentApplicationSlide === 0) {
			pickSlide({
				section: 'applications',
				slide: (applicationSlides.length - 1),
				totalSlides: applicationSlides.length,
				changeCurrentSlide: (i)=> { currentApplicationSlide= i; }
			});
			return;
		}
		pickSlide({
			section: 'applications',
			slide: currentApplicationSlide - 1,
			totalSlides: applicationSlides.length,
			changeCurrentSlide: (i)=> { currentApplicationSlide= i; }
		});
	}
	const rightCarouselController= document.querySelector('div.right-carousel-controller#applications');
	rightCarouselController.onclick= ()=> {
		if (currentApplicationSlide === (applicationSlides.length - 1)) {
			pickSlide({
				section: 'applications',
				slide: 0,
				totalSlides: applicationSlides.length,
				changeCurrentSlide: (i)=> { currentApplicationSlide= i; }
			});
			return;
		}
		pickSlide({
			section: 'applications',
			slide: currentApplicationSlide + 1,
			totalSlides: applicationSlides.length,
			changeCurrentSlide: (i)=> { currentApplicationSlide= i; }
		});
	}
}


const initializeSystemsCarousel= (lang, slides_)=> {
	let systemSlides= slides_;
	const fragment= document.querySelector('div.fragment#systems');
	const slides= document.querySelector('div.slides#systems');

	// Creating Slides
	for (let s of slides_) {
		const fragmentSlide= document.createElement('div');
		fragmentSlide.classList.add('fragment-slide');
		fragmentSlide.classList.add('systems');
		fragmentSlide.setAttribute('id', `fragment-slide-${slides_.indexOf(s)}`);
		fragmentSlide.style.backgroundImage= `url(../images/covers/${s["id"]})`
		

		const title= document.createElement('h3');
		title.innerHTML= s["title"];
		title.innerText= s["title"];
		title.innerTEXT= s["title"];

		const paragraph= document.createElement('p');
		paragraph.innerHTML= s["short_brief"];
		paragraph.innerText= s["short_brief"];
		paragraph.innerTEXT= s["short_brief"];

		const action= document.createElement('a');
		action.innerHTML= lang == "en" ? "See More!" : "إقرأ المزيد!"
		action.classList.add('main-button');
		action.setAttribute('href', s["action"]);

		const actionsDiv= document.createElement('div');
		actionsDiv.classList.add('actions');
		actionsDiv.appendChild(action);

		const contentDiv= document.createElement('div');
		contentDiv.classList.add('content');
		contentDiv.appendChild(title);
		contentDiv.appendChild(paragraph);
		contentDiv.appendChild(actionsDiv);

		fragmentSlide.appendChild(contentDiv);
		fragment.appendChild(fragmentSlide)

		fragment.appendChild(fragmentSlide);
	}

	// Creating Slides Controllers
	for (let i= 0; i!= systemSlides.length; i++) {
		let slide= document.createElement('div');
		slide.classList.add('carousel-slide');
		slide.classList.add('systems');
		slide.setAttribute('id', `slide-${i}`);
		slide.onclick= ()=> {
			pickSlide({
				section: 'systems',
				slide: i,
				totalSlides: systemSlides.length,
				changeCurrentSlide: (i)=> { currentSystemSlide= i; }
			})
		}
		slides.appendChild(slide);

	}
	// Carousel Controllers
	const leftCarouselController= document.querySelector('div.left-carousel-controller#systems');
	leftCarouselController.onclick= ()=> {
		if (currentSystemSlide === 0) {
			pickSlide({
				section: 'systems',
				slide: (systemSlides.length - 1),
				totalSlides: systemSlides.length,
				changeCurrentSlide: (i)=> { currentSystemSlide= i; }
			});
			return;
		}
		pickSlide({
			section: 'systems',
			slide: currentSystemSlide - 1,
			totalSlides: systemSlides.length,
			changeCurrentSlide: (i)=> { currentSystemSlide= i; }
		});
	}
	const rightCarouselController= document.querySelector('div.right-carousel-controller#systems');
	rightCarouselController.onclick= ()=> {
		if (currentSystemSlide === (systemSlides.length - 1)) {
			pickSlide({
				section: 'systems',
				slide: 0,
				totalSlides: systemSlides.length,
				changeCurrentSlide: (i)=> { currentSystemSlide= i; }
			});
			return;
		}
		pickSlide({
			section: 'systems',
			slide: currentSystemSlide + 1,
			totalSlides: systemSlides.length,
			changeCurrentSlide: (i)=> { currentSystemSlide= i; }
		});
	}
}

const pickSlide= (props)=> {
	const slides= document.querySelector(`div.${props.section}.slides#${props.section}`);
	for (let i= 0; i!= props.totalSlides; i++) {
		let slide= document.querySelector(`div.${props.section}.carousel-slide#slide-${i}`);
		const fragmentSlide= document.querySelector(`div.${props.section}.fragment-slide#fragment-slide-${i}`)
		if(props.slide === i) {
			slide.classList.add('active');
			fragmentSlide.classList.add('active');
			props.changeCurrentSlide(i);
		} else {
			slide.classList.remove('active');
			fragmentSlide.classList.remove('active')
		}
	}
}
