# Theoretical Foundations

## Performance Testing Overview

### Non-functional Testing

**Non-Functional Testing** is the process of evaluating aspects of the software that are not related to its functionality. Instead of focusing on testing specific features, it concentrates on factors such as performance, security, reliability, user interaction, and compatibility. The goal of non-functional testing is to ensure that the software performs well not only from a functional perspective but also from other aspects.

### What is Performance Testing?

**Performance Testing** is the process of checking whether a software program runs fast, responds quickly, handles load well, how it uses resources (CPU, RAM, bandwidth, etc.), and whether it can scale to accommodate many concurrent users.

Simply put, the goal of performance testing is to detect and eliminate points that cause the software to run slow, become congested, or fail to meet desired performance levels. Performance testing focuses on the **speed and stability** of the software in real-world use, rather than testing the correctness of its functionality.

The focus of **Performance Testing** is to check for issues in the software program such as:

-   **Speed** - Determines if the application responds quickly.
-   **Scalability** - Determines the maximum user load the software application can handle.
-   **Stability** - Determines if the application is stable under varying loads.

**Performance Testing** is often used to help identify bottlenecks in a system, establish a baseline for future testing, support effective performance tuning, determine compliance with performance goals and requirements, and gather other relevant operational data to help stakeholders make decisions related to the overall quality of the applications being tested. Additionally, the results from performance testing and analysis can help you estimate the hardware configuration needed to support the applications when you release the product for widespread use.

### Types of Performance Testing

#### Load testing

**Load testing** is performed to evaluate the system's behavior under increasing load (number of concurrent users/CCU, number of transactions/requests, etc.), to **determine the maximum load (threshold)** that the system can handle.

![Load Testing](images/image-1.png)

A tip to find the threshold quickly is to double the number of concurrent requests sent to the system with each test. For example:

-   Test 1: Send 3000 concurrent requests
-   Test 2: Send 6000 concurrent requests
-   Test 3: Send 12000 concurrent requests

If the system becomes overloaded in Test 3, then in Test 4, reduce the number of requests added in Test 3 by half, meaning:

-   Test 4: Send 9000 concurrent requests

#### Stress testing

![Stress Testing](images/image-2.png)

**Stress testing** is performed to evaluate the system's behavior when the load exceeds the threshold, to find the breaking point and assess the system's ability to recover.

#### Spike Testing

![Spike Testing](images/image-3.png)

**Spike testing** is performed to evaluate the system's behavior when the load **suddenly increases for a short period**. Some real-world scenarios that require spike testing:

-   E-commerce platforms like Shopee, Lazada, etc., have many large flash sales on holidays and special days.
-   Course registration systems for university students.
-   Systems for selling football tickets, concert tickets, etc.
-   Live streaming systems.

#### Endurance Testing (Soak Testing)

![Soak Testing](images/image-4.png)

**Endurance testing** is performed over a long period to evaluate the system's resource usage (memory). Typically, it runs at 70-80% of the system's threshold for more than 8 hours.

#### Scalability Testing

**Scalability testing (or Capacity testing)** is a type of testing that aims to evaluate the application's ability to handle load as the number of users or transactions increases. This type of testing helps collect the necessary metrics to forecast and determine the appropriate hardware configuration, ensuring the system can meet larger usage demands in the future.

The main purpose of this testing is to support **system sizing** and to check the application's scalability as its scale increases.

**Scalability testing** can be considered the **next step** after load testing when a business needs to prepare for growth and expand its user base in the future.

#### Volume Testing

**Volume testing** is a type of performance testing that aims to evaluate the software or application's ability to handle a **very large amount of data** in the database.

The main goal is to check if the system remains stable, fast, and error-free when accessing, processing, reporting, or synchronizing with **huge amounts of data**.

-   **Example:** Testing the report generation feature when the database has millions of records, or checking the data synchronization speed between large systems.

### Common System Performance Issues

Most performance issues revolve around speed, response time, load time, and poor scalability. Speed is often one of the most important attributes of an application. A slow application wastes time, reduces user satisfaction with the system, and can lead to the loss of potential users. Performance testing is done to ensure the application runs fast enough to attract and maintain user interest and satisfaction.

Below is a list of some common performance issues, which also highlights that speed is the most common factor:

-   ***Long load time*:** Load time is typically the initial time it takes for an application to launch. This should generally be kept to a minimum. While some applications cannot load in under a minute, a load time of a few seconds is ideal.
-   ***Slow response time*:** Response time is the time it takes from when a user inputs data into the application until the application provides a response to that input. Generally, this should be very fast. Again, if users have to wait too long, they will lose interest.
-   ***Poor scalability*:** A software product has poor scalability if it cannot handle the expected number of users or if it does not meet the needs of a sufficient range of users. Load testing must be performed to ensure the application can handle the anticipated number of users.
-   ***Bottlenecks*:** These are obstacles in the system that degrade the overall system performance. A bottleneck occurs when coding errors or hardware issues cause a drop in throughput under a certain load. Bottlenecks are often caused by a faulty piece of code. The key to fixing the problem is to perform bottleneck testing to find the section of code causing the slowdown and find a solution. Some common performance bottlenecks are: CPU, memory, network, operating system, and hard drive.

### Common Metrics in Performance Testing

Depending on the scope of the test and the type of system being tested *(e.g., a web application or a mobile application)*, the measurement parameters or information to be collected and monitored will vary. Below are the general parameters/information often collected and monitored during performance testing:

-   **Processor usage** – The amount of time the processor (CPU) spends executing processing threads.
-   **Memory usage** – The amount of temporary memory (RAM) used to execute requests. This helps evaluate system performance for optimization.
-   **Disk I/O** – The amount of time the disk is busy performing a read or write request.
-   **Disk queue length** – The average number of read and write requests queued for the selected disk over a period of time.
-   **Bandwidth** – Shows the number of bits per second (bits/s – representing network speed) used during the test.
-   **Network output queue length** – The length of the output queue of packets. A queue length greater than one indicates delays and congestion.
-   **Response time** – The time from when a user makes a request until the first response is received from the system (server).
-   **Throughput** – Measures the number of requests per unit of time, usually seconds. Represents the **total number of requests/unit of time** over a period.
-   **Hits per second** – The number of hits/requests sent to the server each second. Often measured during load testing.
-   **Thread counts** – The number of currently running and active threads indicates the "health" of the system.

\newpage
