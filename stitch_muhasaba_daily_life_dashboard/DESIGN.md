---
name: Modern Muhasaba Aesthetic
colors:
  surface: '#111318'
  surface-dim: '#111318'
  surface-bright: '#37393f'
  surface-container-lowest: '#0c0e13'
  surface-container-low: '#1a1b21'
  surface-container: '#1e1f25'
  surface-container-high: '#282a2f'
  surface-container-highest: '#33353a'
  on-surface: '#e2e2e9'
  on-surface-variant: '#d0c5b2'
  inverse-surface: '#e2e2e9'
  inverse-on-surface: '#2e3036'
  outline: '#99907e'
  outline-variant: '#4d4637'
  surface-tint: '#e6c364'
  primary: '#e6c364'
  on-primary: '#3d2e00'
  primary-container: '#c9a84c'
  on-primary-container: '#503d00'
  inverse-primary: '#755b00'
  secondary: '#4ae183'
  on-secondary: '#003919'
  secondary-container: '#06bb63'
  on-secondary-container: '#00431f'
  tertiary: '#a5c9ff'
  on-tertiary: '#00315d'
  tertiary-container: '#70aeff'
  on-tertiary-container: '#004078'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe08f'
  primary-fixed-dim: '#e6c364'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#584400'
  secondary-fixed: '#6bfe9c'
  secondary-fixed-dim: '#4ae183'
  on-secondary-fixed: '#00210c'
  on-secondary-fixed-variant: '#005228'
  tertiary-fixed: '#d4e3ff'
  tertiary-fixed-dim: '#a4c9ff'
  on-tertiary-fixed: '#001c39'
  on-tertiary-fixed-variant: '#004884'
  background: '#111318'
  on-background: '#e2e2e9'
  surface-variant: '#33353a'
typography:
  display-lg:
    fontFamily: Chivo
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Chivo
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Chivo
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-bold:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  arabic-display:
    fontFamily: Cairo
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 52px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base-unit: 4px
  container-margin: 20px
  gutter: 16px
  touch-target: 48px
  card-gap: 12px
---

## Brand & Style

The design system is engineered for the modern, disciplined Muslim man who seeks to balance spiritual excellence with physical and mental ambition. The aesthetic, described as "street-meets-deen," merges the raw, high-contrast energy of urban streetwear branding with the clean, structured minimalism of high-end productivity tools.

The visual language is unapologetically masculine: sharp, high-contrast, and functional. It avoids unnecessary ornamentation, focusing instead on clarity of intent and "muhasaba" (self-reflection). The interface should feel like a cockpit for the soul—precise, reliable, and empowering. It evokes a sense of "Ambitious Brotherhood," where technology serves as a tool for ancient wisdom.

## Colors

This design system utilizes a "Deep Shadow" palette to minimize eye strain during late-night reflections or early-morning Fajr sessions. 

- **Neutral Base:** A very dark, matte charcoal-navy serves as the canvas, providing a sophisticated alternative to pure black.
- **Spiritual Gold:** Reserved for high-priority religious obligations, sunnah highlights, and moments of achievement. It represents the "value" of time.
- **Physical Emerald:** Used for health, strength training, and vitality metrics. It signals growth and life.
- **Mental Blue:** Used for deep work, study, and professional habit tracking. It denotes focus and clarity.

All accent colors must maintain a high contrast ratio against the dark background to ensure glanceability in varied lighting conditions.

## Typography

The typography strategy is built for bilingual efficiency (RTL/LTR). **Chivo** provides a confident, heavy-set weight for headlines that feels impactful and direct. **Hanken Grotesk** offers a contemporary, sharp feel for body text, ensuring high legibility for long-form reflections. **Geist** is utilized for technical data and labels, emphasizing the "dashboard" nature of the system.

For Arabic scripts, the system prioritizes **Cairo** or **Tajawal** to maintain the sharp, modern aesthetic while ensuring traditional characters remain legible at small sizes. All typography is optimized for Right-to-Left (RTL) reading flows, with specific attention paid to line heights to accommodate the vertical strokes of Arabic calligraphy.

## Layout & Spacing

This design system employs a **mobile-first, 4-column fluid grid** for handheld devices, expanding to a **12-column fixed grid** on desktop. 

The rhythm is governed by a 4px baseline, but interaction points are oversized. Given the "daily life" nature of the dashboard, large tap targets (minimum 48px) are mandatory for logging habits on the go. The layout follows a strict RTL (Right-to-Left) orientation: progress bars, toggle directions, and navigation flows must reflect this cultural context. Spacing between card modules should be generous enough to maintain "visual breathing room" despite the dark, heavy color palette.

## Elevation & Depth

To maintain the "sharp" and "disciplined" feel, the design system avoids heavy, diffused shadows. Depth is instead created through **Tonal Layering** and **Low-Contrast Outlines**:

1.  **Base Layer:** The darkest charcoal (#0d0f14) used for the main background.
2.  **Surface Layer:** A slightly lighter navy-grey (#161920) for primary cards and sections.
3.  **Active Outlines:** Instead of shadows, active states or "focused" habits are indicated by a 1px solid border in the respective category color (Gold, Emerald, or Blue) with a very subtle outer glow (4px blur, 10% opacity).
4.  **Glassmorphism (Minimal):** Semi-transparent overlays are used only for fixed navigation bars to show the content passing beneath, using a backdrop blur of 12px.

## Shapes

The shape language is "Soft-Technical." By utilizing **Level 1 (Soft)** roundedness, the UI retains a disciplined, architectural feel without appearing aggressive or "stabby." 

- **Primary Elements:** 4px (0.25rem) radius for buttons and input fields to maintain a precision-tool look.
- **Containers:** 8px (0.5rem) for main dashboard cards, providing a modern but grounded structure.
- **Status Indicators:** Small circles for "Active" states, providing a clean contrast to the rectangular nature of the rest of the UI.

## Components

### Cards
Cards are the primary organizational unit. They use a solid background (#161920) with a subtle 1px border (#242933). Top-border accents (3px height) in Gold, Emerald, or Blue indicate the life-pillar category.

### Custom Toggles
Toggles should feel mechanical and "heavy." Use a sliding rectangular switch rather than a rounded pill. When active, the background should fill with the accent color, and the "knob" should be a crisp white.

### Number Inputs (Dhikr/Muhasaba)
Inputs for counting (e.g., Tasbih or habit reps) must be full-width on mobile with large "+" and "-" hit areas. Use the **Geist** font for numerals to emphasize technical precision.

### Buttons
- **Primary:** Solid Gold with black text for maximum impact.
- **Secondary:** Outlined Emerald or Blue for physical/mental actions.
- **Tertiary:** Ghost buttons with white text for "Cancel" or "Back" actions.

### Progress Bars
RTL progress bars that fill from right to left. Use a "thick" track (8px) with a rounded-sm cap. For spiritual goals, use a gradient from Gold to a brighter Yellow to indicate light and progress.

### Lists
Lists use clean dividers with 10% opacity white. Each item should have a clear "leading" icon in a category-specific color to aid rapid scanning.