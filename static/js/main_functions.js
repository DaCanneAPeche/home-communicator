const burgerMenuButton = document.querySelector("button.burger-menu");
export const setUpBurgerMenuButton = () => {
	burgerMenuButton.addEventListener("click", () => {
		burgerMenuButton.classList.toggle("active");
	})

};

export const setUpExecuteButtons = socket => {

	document.querySelectorAll(".scripts-list div.execute").forEach(script => {
		script.addEventListener("click", () => {
			socket.emit(`/scripts/${script.innerText}`);
		});
	});

	document.querySelectorAll(".pages-list a.execute").forEach(page => {
		page.href = `/pages/${page.innerText}`;
	});

};

const favoritesButtons = document.querySelectorAll(".favorite-button");
export const setUpFavoritesButtons = socket => {
	
	favoritesButtons.forEach(el => {
		
		el.addEventListener("click", () => {
			el.classList.toggle("active");
			const script = el.previousElementSibling.innerText;

			if (el.classList.contains("active")) {
				socket.emit("add-favorite", script);
			}
			else {
				socket.emit("remove-favorite", script);
			}
		
		})
	})


};

export const updateFavoritesButtons = favorites => {

	let favoritePages = [];
	let favoriteScripts = [];

	favorites.forEach(favorite => {
		if (favorite["is_a_page"] === false) {
			favoriteScripts.push(favorite["name"]);
		} else {
			favoritePages.push(favorite["name"]);
		}
	});

	favoritesButtons.forEach(button => {
		const scriptName = button.previousElementSibling.innerText;
		const isAPage = button.parentNode.parentNode.classList.contains("pages-list");

		if ((!isAPage && favoriteScripts.includes(scriptName)) ||
			(isAPage && favoritePages.includes(scriptName))) {
			button.classList.add("active");
		} else {
			button.classList.remove("active");
		}

	});

};

