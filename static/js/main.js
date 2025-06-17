import { setUpExecuteButtons, setUpBurgerMenuButton,
	setUpFavoritesButtons, updateFavoritesButtons } from "./main_functions.js";

socket.on("connect", () => {
	console.log("Socket connection established");
});

setUpBurgerMenuButton();
setUpExecuteButtons(socket);
setUpFavoritesButtons(socket);

socket.emit("get-favorites", "", favorites => {
	updateFavoritesButtons(favorites, socket);
});

socket.on("favorites-change", favorites => {
	updateFavoritesButtons(favorites, socket);
});
