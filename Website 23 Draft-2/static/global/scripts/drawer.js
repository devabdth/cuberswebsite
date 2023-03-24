
const openDrawer = () => {
    // TODO
    const drawer = document.getElementById('drawer');
    const drawerOverlay = document.getElementById('drawer-overlay');
    drawer.style.left = "0";
    drawerOverlay.style.display = "block";
}

const closeDrawer = () => {
    const drawer = document.getElementById('drawer');
    const drawerOverlay = document.getElementById('drawer-overlay');
    drawer.style.left = "-70%";
    drawerOverlay.style.display = "none";
}
