const favoritesWrapper = document.querySelector(".favorites-wrapper");
const updateFavoritesSection = (favorites, socket) => {
	console.log(typeof favorites);
		
	favoritesWrapper.innerHTML = "";
	if (favorites.length === 0) {return}

	let favoritesRows = [];
	let numberOfRows = favorites.length;
	if (numberOfRows > 3) {
		numberOfRows = 3
	}
	for (let index = 0; index < numberOfRows ; index++) {
		let div = document.createElement('div');
		div.classList.add("favorites-row");
		favoritesRows.push(div);
	}

	console.log(typeof favorites);
	favorites.forEach((el, i) => {
    let container = document.createElement('div')
		let div = document.createElement('div');
		div.classList.add("favorite");
		container.classList.add("favorite-container");
		div.innerHTML = el["name"]
		div.setAttribute("is_a_page", el["is_a_page"])

		favoritesRows[i%3].appendChild(container);
    container.appendChild(div)
	});

	favoritesRows.forEach((row) => {
		favoritesWrapper.appendChild(row);
	});

	// updateFavoriteButtons(favorites);
	// updateFavoriteButtonsActions();

	document.querySelectorAll(".favorites-wrapper .favorite").forEach( el => {
		el.addEventListener("click", () => {
			if (el.getAttribute("is_a_page") === "false") {
				socket.emit(`/scripts/${el.innerText}`);
			} 
			else {
				document.location.href = `/pages/${el.innerText}`;
			}
		});
	});

};

socket.emit("get-favorites", "", favorites => {
	updateFavoritesSection(favorites, socket);
});

socket.on("favorites-change", favorites => {
	updateFavoritesSection(favorites, socket);
});

