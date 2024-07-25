import { Article } from '@/components/article'
import { Layout } from '@/components/layout'
import vision_image from '../assets/about_us_images/vision.png'
import mission_image from '../assets/about_us_images/mission.png'
import values_image from '../assets/about_us_images/values.png'
import about_image from '../assets/about_us_images/about_us.webp'

function AboutPage() {
  return (
    <Layout>
      <Article
        title="Who We Are"
        imageAlt="Lorem Picsum"
        imageSrc="https://picsum.photos/420/640?grayscale"
      >
         <div className='flex flex-row'>
        
        {/* <div className='flex flex-col' style={{width:'100%'}}> */}
          
          <div className='flex flex-col' style={{width:'100%'}}>      

            {/* <h2 className="text-1xl mt-3 font-semibold text-gray-800 dark:text-white">Who We Are</h2>   */}
            <div style={{width:'100%'}}>
             
             <img src={about_image} alt="Vision"  />
       </div>
            <p className="mb-1 mt-1 text-gray-500 dark:text-gray-400">
              
            AfriJour serves as a beacon illuminating the rich spectrum of African scholarship and thought. We are committed to amplifying the voices of African journals, providing a platform where their narratives and perspectives can shine brightly. With an unwavering dedication to excellence and inclusivity, we strive to be the foremost destination for exploring the depth and breadth of African academic discourse.
              
               </p>       

                 <hr style={{width:'10%', height:'3px',marginTop:'2rem', background:'#9CE0FE'}}/>  
          

            <h2 className="text-1xl mt-16 font-semibold text-gray-800 dark:text-white">Our Mission</h2>  
            <div style={{display: 'inline-flex', width:'100%'}}>
              <div style={{width:'70%'}}>
             
                      <img src={mission_image} alt="Vision"  />
                </div>
                <div>
                    <p className="mb-1 mt-0 text-gray-500 dark:text-gray-400 ml-5">
                    Our mission at AfriJour is to spotlight and elevate African journals, fostering a global appreciation for the intellectual richness and diversity emanating from the continent. Through innovative analytics and dedicated curation, we aim to empower African scholars and researchers, catalyzing collaboration and knowledge exchange on a global scale. We are driven by a passion for promoting African scholarship and advancing the collective understanding of Africa's multifaceted narratives.
                    </p>  
                </div>
               
               
            </div>
            <hr style={{width:'10%', height:'3px',marginTop:'2rem', background:'#00C95F'}}/>            

            <h2 className="text-1xl mt-16 font-semibold text-gray-800 dark:text-white">Our Vision</h2>  
            <div style={{display: 'inline-flex', width:'100%'}}>             
                <div>
                    <p className="mb-1 mt-0 text-gray-500 dark:text-gray-400 ml-0">
                    Our vision is to be the premier gateway to African journals, fostering a vibrant ecosystem of scholarly exchange and discovery. We aspire to be a catalyst for the global recognition and appreciation of African scholarship, providing a dynamic platform for the exploration and dissemination of African knowledge. By championing the diversity and depth of African academic thought, we seek to inspire and empower the next generation of African scholars and thought leaders.
                    </p>  
                </div>
                <div style={{width:'70%'}}>
             
                      <img src={vision_image} alt="Vision"  />
                </div>
            </div>

            <hr style={{width:'10%', height:'3px',marginTop:'2rem', background:'#0042B8'}}/>  


          </div>
        </div>
       
      </Article>
    </Layout>
  )
}

export default AboutPage
