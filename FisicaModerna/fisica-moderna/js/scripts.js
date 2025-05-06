// Scripts personalizados para el sitio web de Física Moderna

document.addEventListener('DOMContentLoaded', function() {
    // Inicializar tooltips de Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Inicializar popovers de Bootstrap
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
    
    // Botón de volver arriba
    var backToTopButton = document.createElement('a');
    backToTopButton.href = '#';
    backToTopButton.className = 'back-to-top';
    backToTopButton.innerHTML = '<i class="bi bi-arrow-up"></i>';
    document.body.appendChild(backToTopButton);
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopButton.classList.add('show');
        } else {
            backToTopButton.classList.remove('show');
        }
    });
    
    backToTopButton.addEventListener('click', function(e) {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // Selector de modo oscuro/claro
    var darkModeToggle = document.getElementById('darkModeToggle');
    if (darkModeToggle) {
        // Verificar preferencia guardada
        if (localStorage.getItem('darkMode') === 'enabled') {
            document.body.classList.add('dark-mode');
            darkModeToggle.checked = true;
        }
        
        darkModeToggle.addEventListener('change', function() {
            if (this.checked) {
                document.body.classList.add('dark-mode');
                localStorage.setItem('darkMode', 'enabled');
            } else {
                document.body.classList.remove('dark-mode');
                localStorage.setItem('darkMode', null);
            }
        });
    }
    
    // Animación para elementos al hacer scroll
    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.animate-on-scroll');
        
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementPosition < windowHeight - 50) {
                element.classList.add('animated');
            }
        });
    };
    
    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll(); // Ejecutar una vez al cargar la página
    
    // Búsqueda en el sitio
    const searchInput = document.getElementById('siteSearch');
    if (searchInput) {
        searchInput.addEventListener('keyup', function(e) {
            if (e.key === 'Enter') {
                const searchTerm = this.value.trim().toLowerCase();
                if (searchTerm.length > 2) {
                    window.location.href = '/busqueda.html?q=' + encodeURIComponent(searchTerm);
                }
            }
        });
    }
    
    // Contador de tiempo de lectura para páginas de sesiones
    const contentElement = document.querySelector('.content-box');
    if (contentElement) {
        const text = contentElement.textContent;
        const wordCount = text.split(/\s+/).length;
        const readingTime = Math.ceil(wordCount / 200); // Asumiendo 200 palabras por minuto
        
        const readingTimeElement = document.getElementById('readingTime');
        if (readingTimeElement) {
            readingTimeElement.textContent = readingTime + ' min de lectura';
        }
    }
    
    // Zoom en imágenes
    const contentImages = document.querySelectorAll('.content-box img:not(.no-zoom)');
    contentImages.forEach(img => {
        img.style.cursor = 'pointer';
        img.addEventListener('click', function() {
            const modal = document.createElement('div');
            modal.className = 'image-zoom-modal';
            modal.innerHTML = `
                <div class="image-zoom-content">
                    <img src="${this.src}" alt="${this.alt}">
                    <p class="image-caption">${this.alt}</p>
                </div>
            `;
            document.body.appendChild(modal);
            
            modal.addEventListener('click', function() {
                this.remove();
            });
        });
    });
    
    // Destacar código en bloques de código
    const codeBlocks = document.querySelectorAll('pre code');
    if (codeBlocks.length > 0 && typeof hljs !== 'undefined') {
        codeBlocks.forEach(block => {
            hljs.highlightBlock(block);
        });
    }
    
    // Inicializar MathJax si está disponible
    if (typeof MathJax !== 'undefined') {
        MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
    }
    
    // Guardar progreso de lectura
    const saveReadingProgress = function() {
        if (contentElement) {
            const scrollPosition = window.scrollY;
            const contentHeight = contentElement.offsetHeight;
            const windowHeight = window.innerHeight;
            const scrollable = contentHeight - windowHeight;
            
            if (scrollable > 0) {
                const scrolled = Math.min(100, Math.floor((scrollPosition / scrollable) * 100));
                
                if (scrolled > 70) { // Considerar como leído si se ha visto más del 70%
                    const currentPage = window.location.pathname;
                    let readPages = JSON.parse(localStorage.getItem('readPages') || '{}');
                    readPages[currentPage] = true;
                    localStorage.setItem('readPages', JSON.stringify(readPages));
                    
                    // Actualizar indicadores visuales
                    const navLink = document.querySelector(`.sidebar-nav-link[href="${currentPage}"]`);
                    if (navLink && !navLink.classList.contains('active')) {
                        navLink.innerHTML += ' <i class="bi bi-check-circle-fill text-success"></i>';
                    }
                }
            }
        }
    };
    
    window.addEventListener('scroll', saveReadingProgress);
    
    // Marcar páginas ya leídas
    const markReadPages = function() {
        const readPages = JSON.parse(localStorage.getItem('readPages') || '{}');
        const navLinks = document.querySelectorAll('.sidebar-nav-link');
        
        navLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (readPages[href] && !link.classList.contains('active') && !link.querySelector('.bi-check-circle-fill')) {
                link.innerHTML += ' <i class="bi bi-check-circle-fill text-success"></i>';
            }
        });
    };
    
    markReadPages();
});

// Función para cambiar entre pestañas con animación
function switchTab(tabId) {
    const tabElement = document.getElementById(tabId);
    if (tabElement) {
        const tabTrigger = new bootstrap.Tab(tabElement);
        tabTrigger.show();
    }
}

// Función para imprimir contenido actual
function printContent() {
    window.print();
}

// Función para compartir contenido
function shareContent() {
    if (navigator.share) {
        navigator.share({
            title: document.title,
            url: window.location.href
        })
        .catch(error => console.log('Error al compartir:', error));
    } else {
        // Fallback para navegadores que no soportan Web Share API
        const dummy = document.createElement('input');
        document.body.appendChild(dummy);
        dummy.value = window.location.href;
        dummy.select();
        document.execCommand('copy');
        document.body.removeChild(dummy);
        
        alert('URL copiada al portapapeles');
    }
}
