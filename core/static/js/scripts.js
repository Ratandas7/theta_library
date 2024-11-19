const openProfile = document.getElementById('open_profile');
const closeProfile = document.getElementById('close_profile');

openProfile.addEventListener('click', () => {
    closeProfile.classList.toggle('hidden');
});


document.addEventListener('click', (event) => {
    if (!closeProfile.classList.contains('hidden') && !openProfile.contains(event.target) && !closeProfile.contains(event.target)) {
        closeProfile.classList.add('hidden');
    }
});


const mobileMenu = document.getElementById('mobile-menu');
const closeMenu = document.getElementById('close_menu');

closeMenu.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});

document.addEventListener('click', (event) => {
    if (!mobileMenu.classList.contains('hidden') && !closeMenu.contains(event.target) && !mobileMenu.contains(event.target)) {
        mobileMenu.classList.add('hidden');
    }
});





const openAccount = document.getElementById('open_account');
const closeAccount = document.getElementById('close_account');

if (openAccount && closeAccount) {
    openAccount.addEventListener('click', () => {
        closeAccount.classList.toggle('hidden');
    });

    document.addEventListener('click', (event) => {
        if (
            !closeAccount.classList.contains('hidden') &&
            !openAccount.contains(event.target) &&
            !closeAccount.contains(event.target)
        ) {
            closeAccount.classList.add('hidden');
        }
    });
}




document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('category_toggle');
    const categorySection = document.getElementById('category_section');
    const expandIcon = document.getElementById('expand-icon');
    const collapseIcon = document.getElementById('collapse-icon');

    if (toggleButton && categorySection && expandIcon && collapseIcon) {
      toggleButton.addEventListener('click', () => {
        
        categorySection.classList.toggle('hidden');

        
        expandIcon.classList.toggle('hidden');
        collapseIcon.classList.toggle('hidden');
      });
    }
  });



document.addEventListener('DOMContentLoaded', () => {
    
    const filterToggleButton = document.getElementById('filterToggleButton');
    const offCanvasMenu = document.getElementById('offCanvasMenu');
    const backdrop = document.getElementById('menuBackdrop');
    const closeMenuButton = document.getElementById('closeMenuButton');

    
    const categoryToggleButton = document.getElementById('category_Mtoggle');
    const categorySection = document.getElementById('category_Msection');
    const expandIcon = document.getElementById('expand-icon');
    const collapseIcon = document.getElementById('collapse-icon');

    
    function toggleOffCanvasMenu() {
      offCanvasMenu.classList.toggle('hidden');
      backdrop.classList.toggle('hidden');
    }

    
    if (filterToggleButton && offCanvasMenu && backdrop && closeMenuButton) {
      filterToggleButton.addEventListener('click', toggleOffCanvasMenu);
      closeMenuButton.addEventListener('click', toggleOffCanvasMenu);
      backdrop.addEventListener('click', toggleOffCanvasMenu);
    }

   
    if (categoryToggleButton && categorySection && expandIcon && collapseIcon) {
      categoryToggleButton.addEventListener('click', () => {
        categorySection.classList.toggle('hidden');
        expandIcon.classList.toggle('hidden');
        collapseIcon.classList.toggle('hidden');
      });
    }
  });



  const message_btn = document.getElementById('message_btn');
  const message_modal = document.getElementById('message_modal');
  
  if (message_btn && message_modal) {
      message_btn.addEventListener('click', () => {
          message_modal.classList.add('hidden');
      });
  }






  