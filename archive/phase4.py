import re

css_path = r'C:\Users\SHEHARYAR HAMD\Desktop\Hackathon\site\style.css'

phase4_css = """
/* ========================================= */
/* PHASE 4: POLISH, INTERACTIONS, RESPONSIVE */
/* ========================================= */

/* Micro-interactions & Hover States */
.glass-card, .kpi-card, .p-factor, .sensor {
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), 
              background 0.4s cubic-bezier(0.16, 1, 0.3, 1),
              box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.glass-card:hover, .kpi-card:hover, .p-factor:hover {
  transform: translateY(-2px);
  background: var(--glass-bg-hover);
  box-shadow: 0 12px 40px rgba(0,0,0,0.3);
}

.tab-btn, .time-toggle, .reset-btn {
  transition: transform 0.2s ease, opacity 0.2s ease;
}
.tab-btn:active, .time-toggle:active, .reset-btn:active {
  transform: scale(0.96);
}

input[type=range]::-webkit-slider-thumb {
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
}
input[type=range]:active::-webkit-slider-thumb {
  transform: scale(1.3);
  box-shadow: 0 0 15px rgba(77, 163, 255, 0.8);
}

/* Smooth numerical transitions */
.val, .gauge-value, .commercial-value, .s-val {
  transition: color 0.3s ease;
}

/* Reduced Blur for Performance on complex grids */
.sensor-strip, .priority-grid {
  backdrop-filter: none;
}

/* ========================================= */
/* RESPONSIVE BREAKPOINTS                    */
/* ========================================= */

/* Tablet Breakpoint */
@media (max-width: 1024px) {
  .app-container {
    padding: 1rem;
    gap: 1rem;
  }
  
  .dashboard-top {
    grid-template-columns: 1fr; /* Stack map and ranking */
    height: auto;
  }
  
  .map-container {
    height: 400px;
  }

  .dashboard-bottom {
    grid-template-columns: 1fr; /* Stack all cards */
  }

  .hero-area {
    grid-template-columns: 1fr 1fr; /* 2x2 grid for hero */
  }

  .glass-nav .menu {
    display: none; /* Hide nav menu on small screens to save space */
  }

  /* Simplify background blurs for performance on tablets */
  body::before { filter: blur(80px); width: 80vw; height: 80vw; }
  body::after { filter: blur(80px); width: 80vw; height: 80vw; }
}

/* Mobile Breakpoint */
@media (max-width: 768px) {
  .hero-area {
    grid-template-columns: 1fr; /* Stack hero completely */
  }
  
  .hero-main {
    flex-direction: column;
    text-align: center;
  }
  
  .priority-grid {
    grid-template-columns: 1fr; /* Stack factors */
  }
  
  .sensor-strip {
    flex-direction: column; /* Stack sensors */
  }

  .impact-grid {
    grid-template-columns: 1fr; /* Stack impact numbers */
    text-align: center;
  }

  /* Disable heavy glass blurs on mobile for pure performance */
  .glass-card, .glass-nav, .weight-sliders-container {
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
  }
}
"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(phase4_css)
