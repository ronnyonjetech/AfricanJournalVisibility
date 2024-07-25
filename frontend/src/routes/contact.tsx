import { Article } from '@/components/article'
import { Layout } from '@/components/layout'

export default function ContactPage() {
  return (
    <Layout>
      
      <Article
        title="Get in Touch"
        imageAlt="Lorem Picsum"
        imageSrc="https://picsum.photos/420/640?grayscale"
      >
   
       <div className='flex flex-row'>
        
          <div className='flex flex-col' style={{width:'100%'}}>
            
            <div className='flex flex-col' style={{width:'90%'}}>      

              <h2 className="text-1xl mt-3 font-semibold text-gray-800 dark:text-white">Email Us on:</h2>  
              <p className="mb-1 mt-1 text-gray-500 dark:text-gray-400">info@aphrc.org </p>

              <h2 className="text-1xl font-semibold text-gray-800 dark:text-white">Call Us on:</h2>  
              <p className="mb-3 mt-1 text-gray-500 dark:text-gray-400">Phone: +254 20 400 1000 </p>


            

              <h2 className="text-1xl mt-16 font-semibold text-gray-800 dark:text-white">Fill the form below:</h2>             


                <form className="w-full mt-5">
                  <div className="mb-5">
                    <label htmlFor="email" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Name</label>
                    <input type="email" id="email" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Joe Smith" required />
                  </div>
                  <div className="mb-5">
                    <label htmlFor="email" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your email</label>
                    <input type="email" id="email" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@flowbite.com" required />
                  </div>
                  <div className="mb-5">
                    <label htmlFor="password" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Message</label>
                    <textarea id="message" rows={4} className="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Write your thoughts here..."></textarea>
                  </div>                 
                  <button type="submit" className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
                </form>


            </div>
          </div>
          <div className = 'mt-3' style={{width:'50%'}}>
          <h2 className="text-1xl  mb-1 font-semibold text-gray-800 dark:text-white">Visit us:</h2>             

            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.9014798773646!2d36.75906557601873!3d-1.2283334355677005!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x182f199410ec9923%3A0x8f410fe6dae7465!2sAPHRC%20Campus!5e0!3m2!1sen!2ske!4v1711018190283!5m2!1sen!2ske" width="600" height="450" style={{border: '0'}} allowFullScreen={true} loading="lazy" referrerPolicy="no-referrer-when-downgrade"></iframe>
            <h2 className="text-1xl font-semibold text-gray-800 dark:text-white">Our Address:</h2>  


              <p className="mb-1 mt-1 text-gray-500 dark:text-gray-400">APHRC Campus,<br/> Manga Close,
              off Kirawa Road, Kitisuru,
              Nairobi, Kenya
              P.O. Box 10787-00100,
              Nairobi, Kenya
              
              </p>
          </div>
        </div>

      </Article>
    </Layout>
  )
}
