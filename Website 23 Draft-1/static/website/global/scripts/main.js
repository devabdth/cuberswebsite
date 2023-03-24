window.onload = () => {
    reflectPreference()

    // now this script can find and listen for clicks on the control
    document
        .querySelector('#theme-toggle')
        .addEventListener('click', onClick)
    header = document.getElementById('header')
    if (window.scrollY >= 100) {
        header.style.backgroundColor = "var(--body-bg-color)";
        header.style.boxShadow = "0 12px 12px 1px #111";

    } else {
        header.style.backgroundColor = "transparent";
        header.style.boxShadow = "none";

    }
    window.onscroll = () => {
        if (window.scrollY >= 100) {
            header.style.backgroundColor = "var(--body-bg-color)";
            header.style.boxShadow = "0 6px 8px 1px #111";

        } else {
            header.style.backgroundColor = "transparent";
            header.style.boxShadow = "none";

        }
    }
}

const storageKey = 'theme-preference'

const onClick = async () => {
    // flip current value
    theme.value = theme.value === 'light'
        ? 'dark'
        : 'light';
    setPreference()

    await fetch(
        `/config/?mode=${theme.value === 'light' ? 'dart' : 'light'}`, {
        method: 'PATCH'
    }
    )

}

const getColorPreference = () => {
    if (localStorage.getItem(storageKey))
        return localStorage.getItem(storageKey)
    else
        return window.matchMedia('(prefers-color-scheme: dark)').matches
            ? 'dark'
            : 'light'
}

const setPreference = () => {
    localStorage.setItem(storageKey, theme.value)
    reflectPreference()
}

const reflectPreference = () => {
    document.firstElementChild
        .setAttribute('data-theme', theme.value)

    document
        .querySelector('#theme-toggle')
        ?.setAttribute('aria-label', theme.value)
}

const theme = {
    value: getColorPreference(),
}

// set early so no page flashes / CSS is made aware
reflectPreference()

// sync with system changes
window
    .matchMedia('(prefers-color-scheme: dark)')
    .addEventListener('change', ({ matches: isDark }) => {
        theme.value = isDark ? 'dark' : 'light'
        setPreference()
    })

window.onload = () => {
    reflectPreference()

    // now this script can find and listen for clicks on the control
    document
        .querySelector('#theme-toggle')
        .addEventListener('click', onClick)
    header = document.getElementById('header')
    if (window.scrollY >= 100) {
        header.style.backgroundColor = "var(--body-bg-color)";
        header.style.boxShadow = "0 12px 12px 1px #111";

    } else {
        header.style.backgroundColor = "transparent";
        header.style.boxShadow = "none";

    }
    window.onscroll = () => {
        if (window.scrollY >= 100) {
            header.style.backgroundColor = "var(--body-bg-color)";
            header.style.boxShadow = "0 6px 8px 1px #111";

        } else {
            header.style.backgroundColor = "transparent";
            header.style.boxShadow = "none";

        }
    }
}


const openDrawer = () => {
    document.getElementById('drawer').style.left = '0%';
    document.getElementById('drawer-overlay').style.left = '0%';
}

const closeDrawer = () => {
    document.getElementById('drawer').style.left = '-61%';
    document.getElementById('drawer-overlay').style.left = '-100%';
}