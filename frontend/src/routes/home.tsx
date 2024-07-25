import { Hero, HeroIllustration } from '@/components/hero'
// import { PartnersCarousel } from '@/components/Carousel'
import { Layout } from '@/components/layout'
// import PartnersCarousel from './../components/carousel/carousel';



export default function HomePage() {
  
  return (
    <Layout>
      
      <Hero
        title="Spotlighting African Journals"
        content="Welcome to AfriJour, your passport to the myriad narratives and viewpoints emanating from the heart of Africa. Our platform is dedicated to showcasing the vibrant tapestry of African journals through the lens of diverse analytics."
        illustration={<HeroIllustration />}
      />
    </Layout>
    
  )
}
